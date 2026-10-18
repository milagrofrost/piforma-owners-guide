"""Validate source/figure completeness and export the approved redesign proof."""
from pathlib import Path
import argparse,json,re,hashlib
import pymupdf as pdf
P=Path(__file__).resolve().parents[1]
arg=argparse.ArgumentParser();arg.add_argument('--iteration',required=True);arg.add_argument('--final',action='store_true');opts=arg.parse_args()
out=P/'output/redesign-2026-10-17';out.mkdir(exist_ok=True)
doc=pdf.open(P/'output/macintosh-piforma-working-proof.pdf')
normal=lambda s:''.join(c.lower() for c in s if c.isalnum())
text='\n'.join(q.get_text() for q in doc)
assert not re.search(r'\brecorded\b',text,re.I)
assert '85%' not in (P/'styles/book.typ').read_text(encoding='utf-8')
assert 'EB Garamond' in (P/'styles/typography.typ').read_text(encoding='utf-8')
preflight=json.loads((P/'output'/f'manuscript-iteration-{opts.iteration}'/'preflight.json').read_text())
assert not preflight['issues'] and not preflight['compiler_warnings']
figures=[]
for f in sorted((P/'manuscript').glob('*.md')):
    for kind,ident,file,caption in re.findall(r'\[(ILLUSTRATION|SCREENSHOT) ([^|]+)\|([^|]+)\|([^\]]+)\]',f.read_text(encoding='utf-8')):
        needle=normal('Figure '+ident+'. '+caption)
        found=[q.number+1 for q in doc if needle in normal(q.get_text())]
        assert len(found)==1,(ident,found)
        figures.append({'figure':ident,'file':file,'pdf_page':found[0]})
for a in json.loads((P/'assets/screenshots/manifest.json').read_text()):
    assert hashlib.sha256((P/a['original']).read_bytes()).hexdigest()==a['sha256']
photo_manifest=P/'verification/interior-photo-sources.json'
if not photo_manifest.exists():photo_manifest=P/'output/interior-photos/source-manifest.json'
for name,h in json.loads(photo_manifest.read_text()).items():
    assert hashlib.sha256((P/'assets/illustrations'/name).read_bytes()).hexdigest()==h
spreads=pdf.open()
for n in range(1,len(doc),2):
    q=spreads.new_page(width=864,height=522)
    q.show_pdf_page(pdf.Rect(0,0,432,522),doc,n)
    if n+1<len(doc):q.show_pdf_page(pdf.Rect(432,0,864,522),doc,n+1)
spreads.save(out/'facing-pages.pdf',deflate=True)
for left in [8,14,20,34,42,60,62,64]:
    n=left//2-1
    if n<len(spreads):spreads[n].get_pixmap().save(out/f'spread-pdf-{left}-{left+1}.png')
lock={str(f.relative_to(P)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted((P/'manuscript').glob('*.md'))}
(out/'manuscript-lock.json').write_text(json.dumps(lock,indent=2),encoding='utf-8')
(out/'figure-locations.json').write_text(json.dumps(figures,indent=2),encoding='utf-8')
summary={'pages':len(doc),'trim_pt':[432,522],'manuscript_figures':len(figures),'figure_captions':'all present once','original_screenshot_and_interior_photo_hashes':'unchanged','compiler_warnings':False,'text_geometry_issues':[],'recorded_in_publication_copy':False,'physical_print_test':False}
(out/'validation.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
if opts.final:
    for q in doc:q.set_trimbox(q.mediabox);q.set_bleedbox(q.mediabox)
    doc.save(P/'output/macintosh-piforma-layout-reviewed.pdf',garbage=4,deflate=True)
print(json.dumps(summary,indent=2))
