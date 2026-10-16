from pathlib import Path
import json, statistics
import pymupdf as pdf
from PIL import Image
P=Path(__file__).resolve().parents[1]
result={}
for name,pages in [('macintosh-plus.pdf',[0,4,8,14,15,19,21]),('macintosh-se.pdf',[0,4,8,16,17,23])]:
    d=pdf.open(P/'references'/name)
    item={'pages':len(d),'distinct_scan_boxes_pt':sorted(set((round(p.rect.width,2),round(p.rect.height,2)) for p in d)),'samples':[]}
    for n in pages:
        p=d[n]; pix=p.get_pixmap(matrix=pdf.Matrix(2,2)); im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        # Find top horizontal red rule, excluding holes and OCR glyphs.
        rows=[]
        for y in range(40,min(260,im.height)):
            xs=[x for x in range(im.width) if (lambda c:c[0]>150 and c[0]>c[1]*1.45 and c[0]>c[2]*1.45)(im.getpixel((x,y)))]
            if len(xs)>im.width*.25: rows.append((y,min(xs),max(xs)))
        rule=None
        if rows:
            ys=[r[0] for r in rows]; xs=[r[1] for r in rows]; xe=[r[2] for r in rows]
            rule={'bbox_pt':[min(xs)/2,min(ys)/2,max(xe)/2,(max(ys)+1)/2],'method':'2x raster threshold; scan skew included'}
        item['samples'].append({'pdf_page':n+1,'box_pt':list(p.rect),'red_rule':rule})
    result[name]=item
(P/'output/reference-measurements.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
