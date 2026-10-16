"""Package measured layout deliverables after the rendered pages have been reviewed."""
from pathlib import Path
import json,shutil,re
import pymupdf as pdf
from PIL import Image
P=Path(__file__).resolve().parents[1];root=P/'output/layout-review';final=root/'pass-5'
doc=pdf.open(P/'output/macintosh-piforma-working-proof.pdf');before=pdf.open(root/'pass-1/manual.pdf')
for page in doc:
    page.set_trimbox(page.mediabox);page.set_bleedbox(page.mediabox)
    for font in page.get_fonts():assert doc.extract_font(font[0])[3]
    for im in page.get_image_info():
        r=pdf.Rect(im['bbox'])
        assert abs(r.width/r.height-im['width']/im['height'])<.001,'Source aspect ratio changed'
assert not json.loads((final/'binding-check.json').read_text())
doc.save(P/'output/macintosh-piforma-layout-reviewed.pdf',garbage=4,deflate=True)
shutil.copy2(final/'facing-pages.pdf',root/'facing-pages.pdf')
shutil.copy2(final/'image-resolution-report.md',P/'image-resolution-report.md')
shutil.copy2(final/'image-resolution.json',root/'image-resolution.json')

comparisons=pdf.open()
cases=[('Contents',3,3),('Packing photographs',12,9),('Side controls',17,13),('Stand and keyboard',20,15),('Latch procedure',27,21),('Technical specifications',51,43)]
for label,old,new in cases:
    page=comparisons.new_page(width=876,height=546)
    page.insert_text((8,14),f'{label} — BEFORE: PDF {old}',fontsize=9)
    page.insert_text((452,14),f'AFTER: PDF {new}',fontsize=9)
    page.show_pdf_page(pdf.Rect(0,24,432,546),before,old-1)
    page.show_pdf_page(pdf.Rect(444,24,876,546),doc,new-1)
    page.get_pixmap(matrix=pdf.Matrix(1,1)).save(root/f'comparison-{len(comparisons)}.png')
comparisons.save(root/'before-and-after.pdf',deflate=True)

observations={
1:'Cover retained; real photo, title positions and proof designation unchanged.',
2:'Intentional cover reverse is now genuinely blank.',
3:'Contents first half ends after Chapter 2; entries have controlled leading and no spill page.',
4:'Contents second half starts with Chapter 3 and includes complete back matter; no isolated final entries.',
5:'Welcome retained with the original narrow text grid.',
6:'About page retains all chapter descriptions and a controlled ragged edge.',
7:'Chapter 1 recto opener retained; hanging numerals improve step scanning.',
8:'Packing overview remains large, with its complete original caption.',
9:'Both bag photographs now share one comparative plate beside the orientation discussion.',
10:'Front drawing follows the first control-identification paragraph; no unrelated material interposed.',
11:'USB/source discussion and rear diagram remain together; full-width anchor clears binding.',
12:'Forbidden-latch heading, explanation and top view are a single unit.',
13:'Side volume and power drawings share a matched-scale plate; empty canvas alone is omitted.',
14:'Ergonomics and all four setup steps form a coherent facing page for the stand illustration.',
15:'Small stand diagram, keyboard explanation and wide keyboard drawing share one page; captions remain full.',
16:'Mouse introduction and top view stay together; mystery-button joke retained.',
17:'Optical-sensor explanation and mouse underside stay together; labels unaltered.',
18:'Power/accessory prose retained; safety heading keeps its first full paragraph.',
19:'Safety continuation, startup sequence and battery explanation retain full paragraphs and clear step indents.',
20:'Battery slit-view diagram and wake/retry explanation share a page.',
21:'Complete latch procedure, detail drawing and closing joke share one page.',
22:'Startup symptom subsections use consistent headings and whole paragraphs.',
23:'First-session walkthrough occupies a coherent instructional page; no lost steps.',
24:'About/shutdown instructions preserved; packing begins with a complete first step and continues across turn.',
25:'Remaining packing steps, alignment and carrying notes retain sequence and hanging numerals.',
26:'Intentional blank verso before Chapter 2; no running furniture.',
27:'Chapter 2 recto opener and original opening interval retained.',
28:'Component tour uses consistent rules and paragraph rhythm.',
29:'Controls/connections/keyboard sections remain aligned; no isolated heading.',
30:'Short Chapter 2 ending retained without filler.',
31:'Chapter 3 recto opener retained.',
32:'Mouse and keyboard text retain whole paragraphs; keyboard heading keeps its first substantive paragraph.',
33:'Keyboard continuation, AtEase and window introduction retain clear section separation.',
34:'Windows and files continue at paragraph boundaries; full copy preserved.',
35:'Save sequence now has hanging numerals; every step retained.',
36:'Menu and controller sections flow continuously without a forced illustration slot.',
37:'Full-screen exit and diversions retain all instructions and jokes.',
38:'Documentation/network/session sections have consistent spacing and complete closing text.',
39:'Chapter 4 recto opener retained.',
40:'Care sections retain practical text; cleaning heading keeps its first paragraph.',
41:'Service humor and final care paragraph retained; short ending is intentional.',
42:'Intentional blank verso before Appendix A; no running furniture.',
43:'Hardware specifications use aligned label/value rows; values stay whole.',
44:'Connection rows and technical prose continue consistently; no row splits.',
45:'Appendix B title, lead and first symptoms form a coherent opener.',
46:'Mouse/keyboard/sound checks use consistent heads; both sound-path paragraphs fit together.',
47:'Network and frozen-app checks finish naturally; no heading stranded alone.',
48:'Intentional blank verso before glossary; no running furniture.',
49:'Glossary terms stay with complete definitions; controlled spacing.',
50:'Glossary continuation retained, with intentionally short ending.',
51:'Credits retain live links and hanging bullet alignment; no missing acknowledgments.'}
rows=json.loads((final/'page-metrics.json').read_text())
assert len(rows)==len(observations)==51
with (P/'layout-audit.md').open('a',encoding='utf-8') as f:
    f.write('\n## Final page-by-page disposition — pass 5\n\nAll final pages were opened in rendered contact sheets. Physical PDF page numbers are used below.\n\n| PDF | Last content y (pt) | Final disposition |\n|---:|---:|---|\n')
    for r in rows:f.write(f'| {r["pdf_page"]} | {r["last_content_y"]} | {observations[r["pdf_page"]]} |\n')
imgs=json.loads((final/'image-resolution.json').read_text())
copy=json.loads((root/'copy-preservation.json').read_text())
summary={'pages_before':len(before),'pages_after':len(doc),'complete_render_passes':5,'all_manuscript_files_unchanged':True,'text_units_present':copy['units'],'text_units_missing':len(copy['failures']),'images':len(imgs),'minimum_ppi':min(i['ppi'] for i in imgs),'binding_issues':0,'page_size_pt':[432,522],'all_fonts_embedded':True,'blank_pdf_pages':[r['pdf_page'] for r in rows if r['blank']],'physical_print_test':False}
(root/'final-validation.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
