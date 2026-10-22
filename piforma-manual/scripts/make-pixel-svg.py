"""Redraw a pixel-art PNG as an SVG of flat squares, so print and zoom stay crisp.
Usage: make-pixel-svg.py source.png pixel-size target.svg  (white pixels are left out)."""
import sys
from PIL import Image
src,size,dst=sys.argv[1],int(sys.argv[2]),sys.argv[3]
im=Image.open(src).convert('L');im=im.resize((im.width//size,im.height//size),Image.NEAREST)
w,h=im.size;px=im.load();rects=[]
for y in range(h):
    x=0
    while x<w:
        v=px[x,y];e=x
        while e+1<w and px[e+1,y]==v:e+=1
        if v<255:rects.append(f'<rect x="{x}" y="{y}" width="{e-x+1}" height="1" fill="#{v:02x}{v:02x}{v:02x}"/>')
        x=e+1
open(dst,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" shape-rendering="crispEdges">\n'+'\n'.join(rects)+'\n</svg>\n')
print(f'{w}x{h} pixels, {len(rects)} runs -> {dst}')
