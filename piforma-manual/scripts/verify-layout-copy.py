"""Preserve source bytes and verify that every manuscript text unit reaches the PDF."""
from pathlib import Path
import re,json,hashlib,argparse
import pymupdf as pdf
P=Path(__file__).resolve().parents[1]
doc=pdf.open(P/'output/macintosh-piforma-working-proof.pdf')
def normal(s):return ''.join(c.lower() for c in s if c.isalnum())
rendered=normal('\n'.join(page.get_text() for page in doc))
args=argparse.ArgumentParser();args.add_argument('--baseline',type=Path,default=P/'verification/manuscript-lock.json');opts=args.parse_args()
lock=json.loads(opts.baseline.read_text())
checks=[];failed=[]
for name,digest in lock.items():
    f=P/name;assert hashlib.sha256(f.read_bytes()).hexdigest()==digest,name
    buf=[]
    def check():
        if not buf:return
        s=' '.join(buf);buf.clear()
        if s.startswith(('[ILLUSTRATION ','[SCREENSHOT ')):s=s.split('|',2)[2].rstrip(']')
        if s.startswith('[RAIL '):s=s[6:].rstrip(']').replace('|',' ',1)
        s=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',s).replace('**','').replace('`','')
        s=re.sub(r'^(?:#+ |\d+\. |- )','',s)
        ok=normal(s) in rendered
        if not ok and name.startswith('manuscript/0'):
            # Raised initials can be extracted in a separate content stream.
            ok=normal(s[1:]) in rendered
        checks.append({'file':name,'text':s[:90],'present':ok})
        if not ok:failed.append(checks[-1])
    for line in f.read_text(encoding='utf-8').splitlines():
        if line.startswith('<!--') or not line.strip():check();continue
        if line.startswith(('#','- ')) or re.match(r'^\d+\. ',line):check();buf.append(line);check()
        else:buf.append(line)
    check()
(opts.baseline.parent/'copy-preservation.json').write_text(json.dumps({'source_hashes':'unchanged','units':len(checks),'failures':failed},indent=2),encoding='utf-8')
print(json.dumps({'unchanged_manuscript_files':len(lock),'text_units':len(checks),'missing':failed},indent=2))
assert not failed,'Some source text was not found in the PDF'
