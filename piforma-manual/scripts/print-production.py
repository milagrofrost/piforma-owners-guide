"""Letter carrier sheets, vector PDF placement, crop marks, duplex cover parity."""
from pathlib import Path
import pymupdf as pdf
P=Path(__file__).resolve().parents[1]
source=pdf.open(P/'output/piforma-owners-guide.pdf'); result=pdf.open()
W,H=432,522
x,y=(612-W)/2,(792-H)/2
trim=pdf.Rect(x,y,x+W,y+H)
for index in [0,None,1,2,3,None]:
    page=result.new_page(width=612,height=792)
    if index is not None: page.show_pdf_page(trim,source,index)
    for cx,cy in [(x,y),(x+W,y),(x,y+H),(x+W,y+H)]:
        sx=-1 if cx==x else 1; sy=-1 if cy==y else 1
        page.draw_line((cx+sx*5,cy),(cx+sx*17,cy),color=(0,0,0),width=.3)
        page.draw_line((cx,cy+sy*5),(cx,cy+sy*17),color=(0,0,0),width=.3)
    page.set_trimbox(trim)
result.set_metadata({'title':'PiForma Owner’s Guide — Letter duplex production sheets'})
result.save(P/'output/piforma-owners-guide-print-production.pdf',garbage=4,deflate=True)
assert len(result)==6
print('Six Letter carrier pages; four content pages; blank cover reverse and final reverse.')
