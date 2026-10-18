"""Extract complete source units for the isolated design study; never edit prose."""
from pathlib import Path
import json,re,base64
D=Path(__file__).resolve().parent;P=D.parent
def units(name):
    s=(P/'manuscript'/name).read_text(encoding='utf-8')
    s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    return [v.strip() for v in re.split(r'\n\s*\n',s) if v.strip()]
def after(a,title,n=1):
    i=a.index(title);return a[i+1:i+1+n]
u=units('01-getting-started.md');v=units('03-how-piforma-works.md');w=units('05-technical-information.md')
start=after(u,'## Starting up the computer',2)
data={'intro':after(u,'# Getting Started')[0],
      'unpack_intro':after(u,'## Unpacking the equipment')[0],
      'startup_steps':re.split(r'\n(?=\d+\. )',start[0]),'silent_note':start[1],
      'battery':after(u,'### Checking the battery',2),
      'bag_caption':next(x for x in u if x.startswith('[ILLUSTRATION 1-1|')).split('|')[2][:-1],
      'bag_position':next(x for x in u if x.startswith('The PiForma is underneath')),
      'controls_intro':after(u,'## Taking a closer look')[0],
      'software':after(v,'## Opening programs with AtEase',2),
      'tech_intro':after(w,'# Technical Information')[0],
      'tech_rows':after(w,'## Hardware inventory and identification')[0].splitlines(),
      'power':after(w,'## Recorded power architecture')[0]}
(D/'selected-copy.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
b=base64.b64encode((P/'assets/illustrations/1.png').read_bytes()).decode()
(D/'atease-detail.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="85 50 660 310" width="660" height="310"><defs><filter id="gray"><feColorMatrix type="saturate" values="0"/></filter></defs><image width="824" height="600" filter="url(#gray)" href="data:image/png;base64,'+b+'"/></svg>',encoding='utf-8')
