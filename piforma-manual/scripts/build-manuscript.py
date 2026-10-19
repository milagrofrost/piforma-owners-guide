"""Single-source Markdown manuscript -> editable Typst includes -> reviewed proof.

The converter intentionally supports the small authoring vocabulary used here;
it raises on unknown HTML instead of silently dropping prose. Generated files
can be inspected, but edit manuscript/*.md then rerun to retain one prose source.
"""
from pathlib import Path
import re, json, argparse, subprocess, hashlib, shutil, os
import pymupdf as pdf
from PIL import Image, ImageDraw
P=Path(__file__).resolve().parents[1]
arg=argparse.ArgumentParser();arg.add_argument('--iteration',default='1');arg.add_argument('--ppi',type=int,default=180);arg.add_argument('--typst',default=None,help='Typst executable; defaults to TYPST_BIN, local tool or PATH');opts=arg.parse_args()
generated=P/'chapters';generated.mkdir(exist_ok=True)
def q(s): return json.dumps(s,ensure_ascii=False)
def plain(s):
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',s)
    return s.replace('**','').replace('`','')
def inline(s):
    result=[];offset=0
    for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',s):
        result.append('#text('+q(plain(s[offset:m.start()]))+')')
        result.append('#link('+q(m[2])+',text('+q(m[1])+'))');offset=m.end()
    result.append('#text('+q(plain(s[offset:]))+')')
    return ''.join(result)
evidence=[]
layout_file=P/'assets/illustration-layout.json'
artwork_layout=json.loads(layout_file.read_text(encoding='utf-8'))['images'] if layout_file.exists() else {}
artwork_sizes=[]
screen_manifest=P/'assets/screenshots/manifest.json'
screen_assets={a['presentation']:a for a in json.loads(screen_manifest.read_text(encoding='utf-8'))} if screen_manifest.exists() else {}
screen_placements=[]
def convert(file):
    lines=file.read_text(encoding='utf-8').splitlines();blocks=[];buf=[];status='editorial-advice';section='';opening=True
    def flush():
        nonlocal buf,opening
        if not buf:return
        text=' '.join(buf);buf=[]
        evidence.append({'file':str(file.relative_to(P)),'section':section,'paragraph_sha256':hashlib.sha256(text.encode()).hexdigest(),'evidence':status,'preview':text[:140]})
        if text.startswith('[SCREENSHOT '):
            m=re.fullmatch(r'\[SCREENSHOT ([^|]+)\|([^|]+)\|(.+)\]',text)
            if not m:raise ValueError('Malformed screenshot: '+text)
            a=screen_assets[m[2]]
            screen_placements.append({**a,'figure':m[1],'caption':m[3]})
            blocks.append(f'#screen-figure({q(m[1])},{q(m[2])},{q(m[3])},width:{a["width_pt"]}pt)')
        elif text.startswith('[ILLUSTRATION '):
            m=re.fullmatch(r'\[ILLUSTRATION ([^|]+)\|([^|]+)\|(.+)\]',text)
            if not m: raise ValueError('Malformed illustration: '+text)
            if not (P/'assets/illustrations'/m[2]).is_file(): raise FileNotFoundError(m[2])
            with Image.open(P/'assets/illustrations'/m[2]) as artwork:
                limits=artwork_layout.get(m[2],{})
                width=min(limits.get('max_width_pt',366),limits.get('max_height_pt',360)*artwork.width/artwork.height)
                artwork_sizes.append({'figure':m[1],'file':m[2],'caption':m[3],'width_pt':round(width,3),'height_pt':round(width*artwork.height/artwork.width,3),'effective_ppi':round(artwork.width*72/width),'pixels':list(artwork.size)})
            blocks.append(f'#wide-illustration({q(m[1])}, {q(m[2])}, {q(m[3])}, width:{width:.3f}pt)')
        elif text.startswith('[PHOTO NEEDED'):
            m=re.match(r'\[PHOTO NEEDED ([^:]+):\s*(.*)\]$',text)
            if not m: raise ValueError('Malformed figure: '+text)
            blocks.append(f'#figure-slot({q(m[1])}, {q(plain(m[2]))})')
        elif text.startswith(('[VERIFY:','[MODEL TO CONFIRM:')):
            copy=re.sub(r'^\[(VERIFY|MODEL TO CONFIRM):\s*','',text).rstrip(']')
            blocks.append(f'#verification({q(plain(copy))})')
        else:
            function='opener' if opening and file.name.startswith(('01-','02-','03-','04-')) else 'para'
            blocks.append(f'#{function}({q(plain(text))})')
        opening=False
    for line in lines:
        if line.startswith('<!-- evidence:'):
            flush();status=line.removeprefix('<!-- evidence:').removesuffix('-->').strip();continue
        if not line.strip():flush();continue
        if line.startswith('# '):
            flush();section=line[2:];
            if file.name=='00-front-matter.md':
                if section=='About this manual':blocks.append(f'#pagebreak()\n#current-title.update({q(section)})\n#heading(level:1,{q(section)})')
            elif file.name=='06-glossary-and-credits.md' and section=='Credits and acknowledgments':blocks.append(f'#pagebreak(to: "odd")\n#current-title.update({q(section)})\n#heading(level:1,{q(section)})')
            # Back-matter notices after the credits: the warranty opens a page, the others follow it.
            elif file.name=='06-glossary-and-credits.md' and section!='Glossary':blocks.append(('#pagebreak()\n' if section=='PiForma Limited Warranty' else '')+f'#current-title.update({q(section)})\n#heading(level:1,{q(section)})')
            continue
        if line.startswith('## '):
            flush();section=line[3:]
            blocks.append(f'#glossary-term({q(section)})' if file.name=='06-glossary-and-credits.md' else f'#heading(level:2,{q(section)})')
            continue
        if line.startswith('### '):flush();section=line[4:];blocks.append(f'#subhead({q(section)})');continue
        m=re.match(r'^(\d+)\. (.*)',line)
        if m:
            flush();blocks.append(f'#instruction({m[1]},text({q(plain(m[2]))}))')
            evidence.append({'file':str(file.relative_to(P)),'section':section,'evidence':status,'preview':line});opening=False;continue
        if line.startswith('- '):
            flush()
            if file.name=='05-technical-information.md' and ': ' in line:
                label,copy=line[2:].split(': ',1)
                blocks.append(f'#spec-row({q(label+":")},text({q(plain(copy))}))')
            else:blocks.append(f'#bullet([{inline(line[2:])}])')
            evidence.append({'file':str(file.relative_to(P)),'section':section,'evidence':status,'preview':line});opening=False;continue
        if '<!--' in line: raise ValueError('Unsupported markup: '+line)
        buf.append(line)
    flush()
    # Adjacent figures listed as a group share one plate, in any chapter.
    by_file={a['file']:a for a in artwork_sizes}
    for group in json.loads(layout_file.read_text(encoding='utf-8')).get('groups',[]):
        indexes=[i for i,b in enumerate(blocks) if b.startswith('#wide-illustration(') and any(q(name) in b for name in group['files'])]
        if not indexes:continue
        assert len(indexes)==len(group['files'])
        assert indexes==list(range(indexes[0],indexes[0]+len(indexes))), 'Only adjacent figures can be grouped'
        items=[]
        for name in group['files']:
            a=by_file[name]
            trim=artwork_layout.get(name,{}).get('empty_canvas_trim')
            trim_arg=',trim:('+','.join(f'{k}:{v}' for k,v in trim.items())+')' if trim else ''
            items.append(f'(id:{q(a["figure"])},file:{q(name)},caption:{q(a["caption"])},width:{a["width_pt"]}pt{trim_arg})')
        blocks[indexes[0]:indexes[-1]+1]=['#figure-group(('+','.join(items)+',),mode:'+q(group.get('mode','columns'))+')']
    # Presentation rules move only figure blocks, never source prose or captions.
    if file.name=='01-getting-started.md':
        # Startup reads as a procedure with its existing silent-chime explanation
        # alongside it. Prose stays in the manuscript in its original order.
        note=next(i for i,b in enumerate(blocks) if b.startswith('#para(') and 'A silent startup does not by itself' in b)
        start=next(i for i,b in enumerate(blocks[:note]) if b.startswith('#heading(level:2,"Starting up the computer"'))+1
        assert all(b.startswith('#instruction(') for b in blocks[start:note])
        note_copy=blocks[note].removeprefix('#para(').removesuffix(')')
        blocks[start:note+1]=['#annotated("The startup chime",'+note_copy+',[\n'+'\n'.join(blocks[start:note])+'\n])']
        for i,b in enumerate(blocks):
            if b.startswith('#wide-illustration("1-1",'):blocks[i]=b.replace('#wide-illustration(', '#illustration-plate(',1)
        setup=next(i for i,b in enumerate(blocks) if b.startswith('#heading(level:2,"Putting it all together"'))
        blocks.insert(setup,'#pagebreak(weak:true)')
        for placement in json.loads(layout_file.read_text(encoding='utf-8')).get('placements',[]):
            i=next(i for i,b in enumerate(blocks) if b.startswith('#wide-illustration(') and q(placement['file']) in b)
            figure=blocks.pop(i)
            anchor=next(i for i,b in enumerate(blocks) if placement['after_text'] in b)
            blocks.insert(anchor+1,figure)
        for keep in json.loads(layout_file.read_text(encoding='utf-8')).get('keep_together',[]):
            start=next(i for i,b in enumerate(blocks) if keep['start'] in b)
            end=next(i for i,b in enumerate(blocks) if keep['end'] in b)
            assert start<=end
            blocks[start:end+1]=['#block(breakable:false)[\n'+'\n'.join(blocks[start:end+1])+'\n]']
    if file.name=='03-how-piforma-works.md':
        start=next(i for i,b in enumerate(blocks) if b.startswith('#heading(level:2,"Opening programs with AtEase"'))
        first,second,screen=blocks[start+1:start+4]
        assert first.startswith('#para(') and second.startswith('#para(') and screen.startswith('#screen-figure("3-1"')
        blocks[start:start+4]=['#pagebreak(weak:true)',blocks[start],
            '#annotated("AtEase",none,[\n'+first+'\n#launcher-detail()\n])',
            '#annotated("Show Desktop",none,[\n'+second+'\n'+screen+'\n])']
    if file.name=='05-technical-information.md':
        i=0
        while i<len(blocks):
            if not blocks[i].startswith('#spec-row('):i+=1;continue
            end=i+1
            while end<len(blocks) and blocks[end].startswith('#spec-row('):end+=1
            blocks[i:end]=['#reference-plate([\n'+'\n'.join(blocks[i:end])+'\n])'];i+=1
    # Keep short care/troubleshooting topics intact, especially the service
    # department joke and the frozen-application recovery sequence.
    if file.name in ['04-caring-for-piforma.md','07-troubleshooting.md']:
        starts=[i for i,b in enumerate(blocks) if b.startswith('#heading(level:2,')]
        for start,end in reversed(list(zip(starts,starts[1:]+[len(blocks)]))):
            blocks[start:end]=['#block(breakable:false)[\n'+'\n'.join(blocks[start:end])+'\n]']
    if file.name=='02-inside-piforma.md':
        i=next(i for i,b in enumerate(blocks) if b.startswith('#heading(level:2,"The battery and charging paths"'))
        blocks.insert(i,'#pagebreak(weak:true)')
    return '\n'.join(blocks)+'\n'
for file in sorted((P/'manuscript').glob('*.md')):
    (generated/(file.stem+'.typ')).write_text('// Generated from '+str(file.relative_to(P))+'; edit Markdown and rebuild.\n#import "../styles/book.typ": *\n#import "../styles/screenshots.typ": screen-figure\n#import "../styles/typography.typ": accent\n'+convert(file),encoding='utf-8')
(P/'research/paragraph-provenance.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf-8')
out=P/'output'/f'manuscript-iteration-{opts.iteration}';out.mkdir(parents=True,exist_ok=True)
(out/'illustration-sizes.json').write_text(json.dumps(artwork_sizes,indent=2),encoding='utf-8')
(out/'screenshot-placements.json').write_text(json.dumps(screen_placements,indent=2),encoding='utf-8')
preview=['// Generated artwork review; uses the same sizes and captions as the manuscript.', '#import "styles/book.typ": *', '#show: book', '#set page(footer:none)']
new_artwork=[a for a in artwork_sizes if re.fullmatch(r'1-[2346][a-e]\.png',a['file'])]
for i,a in enumerate(new_artwork):
    if i:preview.append('#pagebreak()')
    preview.append(f'#wide-illustration({q(a["figure"])},{q(a["file"])},{q(a["caption"])},width:{a["width_pt"]}pt)')
(P/'artwork-preview.typ').write_text('\n'.join(preview)+'\n',encoding='utf-8')
local_typst=P.parent/'PiForma_Guide_v2/typst.exe'
typst=opts.typst or os.environ.get('TYPST_BIN') or (str(local_typst) if local_typst.exists() else 'typst');logs=[]
def call(args):
    r=subprocess.run(args,capture_output=True,text=True);logs.append(' '.join(args)+'\n'+r.stdout+r.stderr);(out/'compile.log').write_text('\n'.join(logs),encoding='utf-8')
    if r.returncode:raise RuntimeError(r.stderr)
for source,name in [('main.typ','macintosh-piforma-working-proof'),('first-chapter.typ','chapter-1-working-proof'),('artwork-preview.typ','new-artwork-proof')]:
    call([typst,'compile',str(P/source),str(P/'output'/f'{name}.pdf')])
call([typst,'compile','--format','png','--ppi',str(opts.ppi),str(P/'main.typ'),str(out/'page-{p}.png')])
doc=pdf.open(P/'output/macintosh-piforma-working-proof.pdf');issues=[];fonts=[]
for i,page in enumerate(doc):
    assert abs(page.rect.width-432)<.01 and abs(page.rect.height-522)<.01
    for b in page.get_text('blocks'):
        if not page.rect.contains(pdf.Rect(b[:4])):issues.append({'page':i+1,'bbox':b[:4],'text':b[4][:100]})
    for item in page.get_fonts():
        embedded=bool(doc.extract_font(item[0])[3]);fonts.append({'page':i+1,'name':item[3],'embedded':embedded});assert embedded
    # Check text-to-text intersections between distinct extracted lines.
    spans=[(pdf.Rect(s['bbox']),s['text']) for b in page.get_text('dict')['blocks'] if 'lines' in b for line in b['lines'] for s in line['spans']]
    for a,(rect,txt) in enumerate(spans):
        for other,otxt in spans[a+1:]:
            intersection=rect & other
            if intersection.width>2 and intersection.height>2:issues.append({'page':i+1,'overlap':[txt[:80],otxt[:80]]})
summary={'pages':len(doc),'size_pt':[432,522],'ppi':opts.ppi,'compiler_warnings':any('warning:' in l for l in logs),'issues':issues,'fonts':fonts,'status':'working proof; factual checks pending'}
(out/'preflight.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
# Contact sheets are small enough to inspect every page, six at a time.
for start in range(0,len(doc),6):
    sheet=Image.new('RGB',(1380,1120),'#ddd');draw=ImageDraw.Draw(sheet)
    for k in range(start,min(start+6,len(doc))):
        im=Image.open(out/f'page-{k+1}.png').convert('RGB');im.thumbnail((432,522));x=(k-start)%3*460+10;y=(k-start)//3*560+24;sheet.paste(im,(x,y));draw.text((x,y-17),f'PDF {k+1}',fill='black')
    sheet.save(out/f'contact-{start//6+1}.png')
plus=pdf.open(P/'references/macintosh-plus.pdf');se=pdf.open(P/'references/macintosh-se.pdf')
for i,idx in enumerate([4,14,15,21]):
    pix=plus[idx].get_pixmap(matrix=pdf.Matrix(opts.ppi/72,opts.ppi/72));ref=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);ref.save(out/f'plus-reference-{idx+1}.png')
for idx in [4,16,17,23]:se[idx].get_pixmap(matrix=pdf.Matrix(opts.ppi/72,opts.ppi/72)).save(out/f'se-reference-{idx+1}.png')
# Pick chapter-opening and instructional pages by extracted headings.
for needle,refindex in [('Getting Started',14),('Unpacking the equipment',15),('Starting up the computer',21)]:
    matches=[i for i,p in enumerate(doc) if needle in p.get_text().splitlines() and 'Contents' not in p.get_text() and i>3]
    if not matches:continue
    i=matches[0];target=Image.open(out/f'page-{i+1}.png').convert('RGB');pix=plus[refindex].get_pixmap(matrix=pdf.Matrix(opts.ppi/72,opts.ppi/72));ref=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    w,h=target.size;canvas=Image.new('RGB',(w*2+24,h+30),'#ddd');canvas.paste(ref,(0,30));canvas.paste(target,(w+24,30));ImageDraw.Draw(canvas).text((5,5),f'Plus PDF {refindex+1} / proof PDF {i+1}: {needle}',fill='black');canvas.save(out/f'comparison-{refindex+1}.png')
print(json.dumps({k:v for k,v in summary.items() if k!='fonts'},indent=2)[:12000])
if issues:raise SystemExit('Preflight found issues; inspect before accepting.')
