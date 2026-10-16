"""Lossless source copies and editable SVG presentation viewports; no pixel repainting."""
from pathlib import Path
import base64,json,hashlib,shutil
from PIL import Image
P=Path(__file__).resolve().parents[1];dest=P/'assets/screenshots';(dest/'originals').mkdir(parents=True,exist_ok=True)
items=[
 (1,'piforma-desktop-overview',None,366),
 (2,'piforma-shutdown-menu',(0,0,460,145),242),
 (3,'piforma-about-system',(0,0,745,490),366),
 (4,'piforma-guide-application',(0,25,824,570),366),
 (5,'piforma-clippy-conversation',(222,124,603,504),242),
 (6,'piforma-control-strip',(0,525,230,602),176),
 (7,'piforma-show-desktop',(0,0,420,120),242),
 (8,'piforma-application-menus',(0,0,824,290),366),
 (9,'piforma-open-home-folder',(0,0,375,140),242),
 (10,'piforma-home-folder',None,366),
 (11,'piforma-clippy-message-entry',(240,438,584,482),242),
]
manifest=[]
for number,name,roi,width in items:
    src=P/'assets/illustrations'/f'{number}.png';raw=src.read_bytes()
    with Image.open(src) as im:w,h=im.size
    bounds=(0,0,w,h) if roi is None else (roi[0],roi[1],min(roi[2],w),min(roi[3],h))
    x,y,right,bottom=bounds;vw=right-x;vh=bottom-y
    assert 0<=x<right<=w and 0<=y<bottom<=h
    shutil.copy2(src,dest/'originals'/f'{name}.png')
    encoded=base64.b64encode(raw).decode('ascii')
    # A viewBox and color matrix affect presentation only. No interface elements move.
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{vw}" height="{vh}" viewBox="{x} {y} {vw} {vh}">
<defs><filter id="gray" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feColorMatrix type="saturate" values="0"/></filter></defs>
<image x="0" y="0" width="{w}" height="{h}" href="data:image/png;base64,{encoded}" filter="url(#gray)"/>
</svg>'''
    (dest/f'{name}.svg').write_text(svg,encoding='utf-8')
    manifest.append({'original':str(src.relative_to(P)),'source_copy':f'assets/screenshots/originals/{name}.png','presentation':f'{name}.svg','sha256':hashlib.sha256(raw).hexdigest(),'pixels':[w,h],'viewport_px':list(bounds),'viewport_size_px':[vw,vh],'width_pt':width,'height_pt':round(width*vh/vw,3),'effective_native_ppi':round(vw*72/width),'treatment':'native pixel geometry; grayscale SVG viewport; lossless color original retained'})
(dest/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps([{k:v for k,v in a.items() if k in ['original','pixels','viewport_px','width_pt','effective_native_ppi']} for a in manifest],indent=2))
