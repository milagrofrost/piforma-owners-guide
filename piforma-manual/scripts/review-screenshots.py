"""Verify screenshot provenance/placement and export current review artifacts."""
from pathlib import Path
import argparse,json,hashlib,re,shutil
import pymupdf as pdf
P=Path(__file__).resolve().parents[1]
arg=argparse.ArgumentParser();arg.add_argument('--iteration',required=True);arg.add_argument('--final',action='store_true');opts=arg.parse_args()
root=P/'output/screenshot-integration';out=root/opts.iteration;out.mkdir(parents=True,exist_ok=True)
run=P/'output'/f'manuscript-iteration-{opts.iteration}'
placements=json.loads((run/'screenshot-placements.json').read_text())
assert len(placements)==11
doc=pdf.open(P/'output/macintosh-piforma-working-proof.pdf')
def normal(s):return ''.join(c.lower() for c in s if c.isalnum())
alltext=normal('\n'.join(page.get_text() for page in doc));result=[]
for a in placements:
    source=P/a['original'];assert hashlib.sha256(source.read_bytes()).hexdigest()==a['sha256']
    assert source.read_bytes()==(P/a['source_copy']).read_bytes()
    needle=normal('Figure '+a['figure']+'. '+a['caption'])
    found=[n for n,page in enumerate(doc) if needle in normal(page.get_text())]
    assert len(found)==1,(a['figure'],found)
    n=found[0];page=doc[n]
    clips=[pdf.Rect(d['scissor']) for d in page.get_drawings(extended=True) if d['type']=='clip']
    for im in page.get_image_info():
        r=pdf.Rect(im['bbox'])
        # MuPDF reports the entire embedded PNG, including pixels outside an
        # SVG viewport. Measure the visible intersection with its crop clip.
        matching=[c for c in clips if r.contains(c) or
                  (c.intersects(r) and abs(c.x0-r.x0)<.2 and abs(c.y0-r.y0)<.2)]
        if matching:r &= max(matching,key=lambda c:(c & r).get_area())
        assert page.rect.contains(r),(n,r)
        # All screenshot SVG viewports remain within trim/binding-safe rectangles.
        inside=r.x0 if n%2==0 else 432-r.x1
        assert inside>=35.9,(n,inside)
    result.append({**a,'pdf_page':n+1})
    page.get_pixmap(matrix=pdf.Matrix(2,2)).save(out/f'figure-{a["figure"]}.png')
    page.get_pixmap().save(out/f'actual-size-{a["figure"]}.png')
# Unrelated manuscript files must remain unchanged.
old=json.loads((root/'before-manuscript-hashes.json').read_text())
for name,h in old.items():
    if Path(name).name not in ['01-getting-started.md','03-how-piforma-works.md']:
        assert hashlib.sha256((P/name).read_bytes()).hexdigest()==h,name
assert normal('persistent system menu bar') in alltext
assert normal('application-local menu bars') in alltext
assert normal('press Enter or click Send') in alltext
assert normal('Clippy’s chat, for example, has its close button at the upper right') in alltext
for page in doc:
    for f in page.get_fonts():assert doc.extract_font(f[0])[3]
spreads=pdf.open()
for n in range(1,len(doc),2):
    page=spreads.new_page(width=864,height=522)
    page.show_pdf_page(pdf.Rect(0,0,432,522),doc,n)
    if n+1<len(doc):page.show_pdf_page(pdf.Rect(432,0,864,522),doc,n+1)
spreads.save(out/'facing-pages.pdf',deflate=True)
shutil.copy2(P/'output/macintosh-piforma-working-proof.pdf',out/'manual.pdf')
(out/'screenshots.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
summary={'pages':len(doc),'screenshots':len(result),'source_PNGs':'all originals and lossless copies unchanged','unrelated_manuscript_files':'unchanged','fonts':'all embedded','placement':'each caption occurs once; screenshot pages within trim/binding clearance','physical_print_test':False}
(out/'validation.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
if opts.final:
    for page in doc:page.set_trimbox(page.mediabox);page.set_bleedbox(page.mediabox)
    doc.save(P/'output/macintosh-piforma-layout-reviewed.pdf',garbage=4,deflate=True)
    shutil.copy2(out/'facing-pages.pdf',root/'facing-pages.pdf')
    report=['# Screenshot integration — placement and native resolution','',f'Full manual: {len(doc)} PDF pages. All 11 supplied screenshots are integrated once. Lossless numbered originals remain unchanged; descriptive PNG copies and SVG grayscale viewports are in assets/screenshots.','', '| Figure | Source | PDF page | Printed width | Native viewport ppi |','|---|---|---:|---:|---:|']
    for a in result:report.append(f'| {a["figure"]} | {Path(a["original"]).name} | {a["pdf_page"]} | {a["width_pt"]/72:.2f} in | {a["effective_native_ppi"]} |')
    report+=['','Native pixel counts are reported honestly. Small menu/strip crops are deliberately enlarged for reading, retaining their pixel appearance. SVG wrapping does not turn a raster capture into vector interface artwork or add detail. Menu labels, icon geometry and controls have not been regenerated.','', 'The Clippy entry crop shows the supplied message field, Enter hint and Send button. The stills do not establish whether a click, double-click or another action opens chat; no opening gesture is invented. Screenshot 8 illustrates command location and the two menu bars, not a successful save. Shutdown capture shows menu selection, not completion.']
    (P/'screenshot-integration-report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
