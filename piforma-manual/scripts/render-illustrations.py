"""Render the hand-drawn SVG illustrations in assets/illustrations/src to PNG.

The manuscript's [ILLUSTRATION] tags take PNG files, so each SVG is rendered
with Typst (which supplies EB Garamond for the labels) at 600 ppi.
"""
from pathlib import Path
import subprocess,os,sys,tempfile
P=Path(__file__).resolve().parents[1]
SRC=P/'assets/illustrations/src';OUT=P/'assets/illustrations'
typst=os.environ.get('TYPST_BIN','typst')
names=sys.argv[1:] or [f.stem for f in sorted(SRC.glob('*.svg'))]
for name in names:
    svg=SRC/f'{name}.svg'
    with tempfile.TemporaryDirectory(dir=P) as tmp:
        doc=Path(tmp)/'render.typ'
        doc.write_text(f'#set page(width:auto,height:auto,margin:0pt,fill:white)\n#image("{os.path.relpath(svg,tmp)}",width:4in)\n')
        subprocess.run([typst,'compile','--root',str(P),'--format','png','--ppi','600',str(doc),str(OUT/f'{name}.png')],check=True)
    print(name)
