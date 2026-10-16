"""Page geometry, actual-size spreads and resolution evidence for a layout pass."""
from pathlib import Path
import argparse,json,hashlib,shutil
import pymupdf as fitz
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('--pass',dest='number',type=int,required=True);args=a.parse_args()
root=P/'output/layout-review';run=root/f'pass-{args.number}';run.mkdir(parents=True,exist_ok=True)
src=P/'output/macintosh-piforma-working-proof.pdf';shutil.copy2(src,run/'manual.pdf')
doc=fitz.open(src);pages=[];images=[];issues=[]
locked=json.loads((root/'manuscript-lock.json').read_text())
assert all(hashlib.sha256((P/f).read_bytes()).hexdigest()==h for f,h in locked.items()),'Manuscript changed during layout work'
spreads=fitz.open()
for n,page in enumerate(doc):
    rect=page.rect;words=page.get_text('words');body=[w for w in words if w[1]<478]
    artwork=page.get_image_info(xrefs=True)
    clips=[d['scissor'] for d in page.get_drawings(extended=True) if d['type']=='clip']
    safe=fitz.Rect(36 if n%2==0 else 24,24,408 if n%2==0 else 396,480)
    for im in artwork:
        r=fitz.Rect(im['bbox']);ppi=min(im['width']*72/r.width,im['height']*72/r.height)
        visible=fitz.Rect(r)
        for clip in clips:
            if abs(clip.x0-r.x0)<.1 and abs(clip.x1-r.x1)<.1 and clip.intersects(r):visible &= clip
        images.append({'pdf_page':n+1,'pixels':[im['width'],im['height']],'size_in':[round(visible.width/72,3),round(visible.height/72,3)],'ppi':round(ppi),'bounds_pt':list(r),'visible_bounds_pt':list(visible),'binding_clearance_pt':round(visible.x0 if n%2==0 else 432-visible.x1,2),'within_trim':rect.contains(visible)})
        if not rect.contains(visible):issues.append({'page':n+1,'image_outside_trim':list(visible)})
        if n>1 and not safe.contains(visible):issues.append({'page':n+1,'image_outside_safe_area':list(visible)})
    # All pages are rendered as standalone images by the build; actual-size review is 72 ppi.
    page.get_pixmap(matrix=fitz.Matrix(1,1)).save(run/f'actual-size-{n+1}.png')
    last=max([w[3] for w in body]+[im['bbox'][3] for im in artwork]+[39])
    pages.append({'pdf_page':n+1,'opening_text':' '.join(w[4] for w in body[:14]),'body_words':len(body),'images':len(artwork),'last_content_y':round(last,1),'unused_lower_pt':round(479-last,1),'blank':len(body)==0 and not artwork,'size_pt':[rect.width,rect.height]})
    if n>1:
        for w in words:
            r=fitz.Rect(w[:4])
            # Footers sit below the body and are checked independently for binding.
            inner=r.x0 if n%2==0 else 432-r.x1
            if inner<35.9:issues.append({'page':n+1,'text_binding_clearance':round(inner,2),'word':w[4]})
for left in range(1,len(doc),2):
    spread=spreads.new_page(width=864,height=522)
    spread.show_pdf_page(fitz.Rect(0,0,432,522),doc,left)
    if left+1<len(doc):spread.show_pdf_page(fitz.Rect(432,0,864,522),doc,left+1)
    spread.get_pixmap(matrix=fitz.Matrix(1.25,1.25)).save(run/f'spread-{left+1}-{left+2}.png')
spreads.save(run/'facing-pages.pdf',deflate=True)
(run/'page-metrics.json').write_text(json.dumps(pages,indent=2),encoding='utf-8')
(run/'image-resolution.json').write_text(json.dumps(images,indent=2),encoding='utf-8')
(run/'binding-check.json').write_text(json.dumps(issues,indent=2),encoding='utf-8')
report=['# Image-resolution report', '',f'Layout pass {args.number}; source images remain unchanged. Dimensions are measured from the PDF, not requested sizes.','', '| PDF page | Pixels | Printed inches | Effective ppi | Binding clearance pt |','|---:|---|---|---:|---:|']
for im in images:report.append(f'| {im["pdf_page"]} | {im["pixels"][0]} × {im["pixels"][1]} | {im["size_in"][0]:.2f} × {im["size_in"][1]:.2f} | {im["ppi"]} | {im["binding_clearance_pt"]:.1f} |')
report+=['','300 ppi is a useful continuous-tone target, and fine raster line work benefits from more. Source resolution alone cannot establish label legibility. Labels are also inspected in the actual-size raster and in 2× page renders. No upsampling is used to claim additional detail. Printer-specific physical proof remains necessary for the smallest raster labels.']
(run/'image-resolution-report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
print(json.dumps({'pass':args.number,'pages':len(doc),'images':len(images),'blank_pages':[p['pdf_page'] for p in pages if p['blank']],'binding_issues':len(issues),'manuscript':'all source hashes unchanged'},indent=2))
