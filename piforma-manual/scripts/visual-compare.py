"""Compile, render, compare, and preflight. Run from any working directory."""
from pathlib import Path
import argparse, subprocess, json, sys
import pymupdf as pdf
from PIL import Image, ImageDraw, ImageOps

P=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--iteration', default='final')
parser.add_argument('--ppi',type=int,default=240)
parser.add_argument('--typst',default=str(P.parent/'PiForma_Guide_v2/typst.exe'))
args=parser.parse_args()
out=P/'output'; run=out/f'iteration-{args.iteration}'; run.mkdir(parents=True,exist_ok=True)
logs=[]
def call(command):
    r=subprocess.run(command,capture_output=True,text=True)
    logs.append('$ '+' '.join(map(str,command))+'\n'+r.stdout+r.stderr)
    (run/'compile.log').write_text('\n'.join(logs),encoding='utf-8')
    if r.returncode: raise RuntimeError(r.stderr)
call([args.typst,'compile',str(P/'prototype.typ'),str(out/'piforma-owners-guide.pdf')])
call([args.typst,'compile','--format','png','--ppi',str(args.ppi),str(P/'prototype.typ'),str(run/'page-{p}.png')])
doc=pdf.open(out/'piforma-owners-guide.pdf')
assert len(doc)==4, f'Expected four pages; got {len(doc)}'
checks={'pages':len(doc),'ppi':args.ppi,'warnings':any('warning:' in s for s in logs),'page_sizes_pt':[],'fonts':[], 'text_outside_page':[], 'raster_images':[]}
for i,page in enumerate(doc):
    assert abs(page.rect.width-432)<.02 and abs(page.rect.height-522)<.02
    checks['page_sizes_pt'].append([page.rect.width,page.rect.height])
    for font in page.get_fonts(full=True):
        embedded=bool(doc.extract_font(font[0])[3])
        checks['fonts'].append({'page':i+1,'name':font[3],'embedded':embedded})
        assert embedded, f'Font not embedded: {font}'
    for b in page.get_text('blocks'):
        if not page.rect.contains(pdf.Rect(b[:4])): checks['text_outside_page'].append([i+1,b[:4]])
    checks['raster_images'].append({'page':i+1,'count':len(page.get_images())})
    Image.open(run/f'page-{i+1}.png').save(out/'page-previews'/f'page-{i+1}.png')
assert not checks['text_outside_page'], checks['text_outside_page']
plus=pdf.open(P/'references/macintosh-plus.pdf'); se=pdf.open(P/'references/macintosh-se.pdf')
for i,idx in enumerate([0,14,15,21]):
    page=plus[idx]; pix=page.get_pixmap(matrix=pdf.Matrix(args.ppi/72,args.ppi/72))
    ref=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    target=Image.open(run/f'page-{i+1}.png').convert('RGB')
    # Same points-to-pixels scale; white padding/cropping instead of scan stretching.
    carrier=Image.new('RGB',target.size,'white');carrier.paste(ref,(0,0));ref=carrier
    ref.save(run/f'reference-{idx+1}.png')
    w,h=target.size; canvas=Image.new('RGB',(w*2+30,h+44),'#dedede'); canvas.paste(ref,(0,44));canvas.paste(target,(w+30,44))
    draw=ImageDraw.Draw(canvas);draw.text((14,14),f'Macintosh Plus: PDF page {idx+1}',fill='black');draw.text((w+44,14),f'PiForma: page {i+1}',fill='black')
    canvas.save(run/f'comparison-{i+1}.png')
    # Overlay shows relative placement, not a numerical fidelity score.
    Image.blend(ref,target,.5).save(run/f'overlay-{i+1}.png')
for idx in [0,4,8,9,11,16,17,23]:
    se[idx].get_pixmap(matrix=pdf.Matrix(args.ppi/72,args.ppi/72)).save(run/f'se-reference-{idx+1}.png')
thumbs=[]
for i in range(4):
    im=Image.open(run/f'page-{i+1}.png').convert('RGB');im.thumbnail((436,523));thumbs.append(im)
sheet=Image.new('RGB',(4*456,563),'#ddd')
for i,im in enumerate(thumbs): sheet.paste(im,(i*456+10,25))
sheet.save(run/'all-pages.png')
(run/'preflight.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
print(json.dumps(checks,indent=2))
