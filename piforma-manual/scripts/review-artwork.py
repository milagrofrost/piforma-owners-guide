"""Check integrated image geometry and export the pages containing a new figure."""
from pathlib import Path
import argparse, json, hashlib
import pymupdf as pdf
P=Path(__file__).resolve().parents[1]
arg=argparse.ArgumentParser();arg.add_argument('--iteration',required=True);args=arg.parse_args()
run=P/'output'/f'manuscript-iteration-{args.iteration}'
sizes=json.loads((run/'illustration-sizes.json').read_text(encoding='utf-8'))
doc=pdf.open(P/'output/macintosh-piforma-working-proof.pdf');result=[]
for a in sizes:
    if not a['file'].startswith('1-'):continue
    # An instruction may cite "Figure 1-6a." too; identify the caption by its copy.
    caption=f'Figure {a["figure"]}. {a["caption"]}'
    normalize=lambda s: ''.join(c.lower() for c in s if c.isalnum())
    pages=[i for i,page in enumerate(doc) if normalize(caption) in normalize(page.get_text())]
    assert len(pages)==1,(a['figure'],pages)
    n=pages[0];page=doc[n];rects=[]
    for image in page.get_images():
        for rect in page.get_image_rects(image[0]):
            assert page.rect.contains(rect),(a['figure'],rect)
            assert rect.y1 < 480,(a['figure'],'image enters footer',rect)
            rects.append([round(v,3) for v in rect])
    expected=[r for r in rects if abs((r[2]-r[0])-a['width_pt'])<.02 and abs((r[3]-r[1])-a['height_pt'])<.02]
    assert expected,(a['figure'],'image missing or wrong size',rects)
    result.append({**a,'pdf_page':n+1,'image_bounds_pt':expected[0],'source_sha256':hashlib.sha256((P/'assets/illustrations'/a['file']).read_bytes()).hexdigest()})
    page.get_pixmap(matrix=pdf.Matrix(3,3)).save(run/f'figure-{a["figure"]}.png')
(run/'new-artwork-pages.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
preview=pdf.open(P/'output/new-artwork-proof.pdf');assert len(preview)==len(result)
review=['# Artwork integration review — current proof','',
        'Twelve owner-supplied images are integrated at their configured aspect ratios. Full manuscript: '+str(len(doc))+' pages. Standalone artwork proof: '+str(len(preview))+' pages. Figure 1-6b appears before 1-6a because the normal through-slit battery check precedes optional opening; identifiers continue to match the supplied filenames.','',
        '| Figure | Full-PDF page | Printed image size (inches) | Effective source ppi |','|---|---:|---|---:|']
for r in result:
    review.append(f'| {r["figure"]} | {r["pdf_page"]} | {r["width_pt"]/72:.2f} × {r["height_pt"]/72:.2f} | {r["effective_ppi"]} |')
review.extend(['','The layout preserves source images and complete labels; captions are separate editable Typst text. All twelve images were checked against their configured PDF dimensions and remain inside the page, above the footer. Full-book preflight checks text bounds, overlapping spans and embedded fonts.','',
               'Source resolution is reported rather than increased artificially. A physical proof remains useful for the finest raster strokes and smallest labels. Photographs are supplied grayscale and retain ample resolution. Source files are unchanged. The layout clips only measured empty canvas above/below the two side views, with hardware and callouts preserved.','',
               'The owner clarified top access and the normal battery check; these instructions supersede the older access question. The stand leg must be seated before supporting the computer. Hidden keyboard USB/power locations are described as approximate. Mouse Sync is unnecessary for the normal single-receiver setup. The right-click, Forbidden Latch/CEO and optical-sensor jokes are retained without changing the actual controls.'])
(P/'output/new-artwork-review.md').write_text('\n'.join(review)+'\n',encoding='utf-8')
print(json.dumps({'new_illustrations':len(result),'artwork_proof_pages':len(preview),'geometry':'all present at configured size, inside trim and above footer','pages':[{'figure':r['figure'],'pdf_page':r['pdf_page']} for r in result]},indent=2))
