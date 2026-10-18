"""Render six trim pages, before/after/reference boards and physical spreads."""
from pathlib import Path
import pymupdf as pdf,json,hashlib,statistics
from PIL import Image,ImageDraw
D=Path(__file__).resolve().parent;P=D.parent
out=D/'renders';out.mkdir(exist_ok=True)
lock=json.loads((D/'production-lock.json').read_text())
assert all(hashlib.sha256((P/n).read_bytes()).hexdigest()==h for n,h in lock.items()),'Production files changed'
study=pdf.open(D/'design-study.pdf');current=pdf.open(P/'output/macintosh-piforma-working-proof.pdf')
assert len(study)==6
overlaps=[]
for q in study:
    assert q.rect==pdf.Rect(0,0,432,522)
    q.set_trimbox(q.mediabox)
    for block in q.get_text('blocks'):assert q.rect.contains(pdf.Rect(block[:4])),block
    for font in q.get_fonts():assert study.extract_font(font[0])[3]
    spans=[(pdf.Rect(s['bbox']),s['text']) for b in q.get_text('dict')['blocks'] for l in b.get('lines',[]) for s in l['spans']]
    for j,(a,t) in enumerate(spans):
        for b,u in spans[j+1:]:
            z=a & b
            if z.width>2 and z.height>2:overlaps.append([q.number+1,t,u])
assert not overlaps,overlaps
def norm(s):return ''.join(c.lower() for c in s if c.isalnum())
copy=json.loads((D/'selected-copy.json').read_text(encoding='utf-8'))
expected=[copy['intro'],copy['unpack_intro'],copy['silent_note'],*copy['battery'],copy['bag_caption'],copy['controls_intro'],*copy['software'],copy['tech_intro']]
expected += [s.split('. ',1)[1] for s in copy['startup_steps']]
expected += [s.removeprefix('- ').replace(': ',' ',1) for s in copy['tech_rows']]
actual=norm('\n'.join(q.get_text() for q in study))
assert all(norm(s) in actual for s in expected),[s[:80] for s in expected if norm(s) not in actual]
current_pages=[7,19,8,13,40,55] # one-based physical PDF pages, not folios
refs=[('macintosh-plus.pdf',15),('macintosh-plus.pdf',22),('macintosh-plus.pdf',17),('macintosh-se.pdf',20),('macintosh-plus.pdf',29),('macintosh-plus.pdf',71)]
labels=['Chapter introduction','Text-led instructions','Bag illustration plate','Grouped hardware controls','Screenshot sequence','Technical reference plate']
boards=pdf.open();two=pdf.open();old=pdf.open();sheet=Image.new('RGB',(1296,1092),'#ddd');draw=ImageDraw.Draw(sheet)
for i,(q,n,(ref,rn)) in enumerate(zip(study,current_pages,refs)):
    for ppi in [72,144]:q.get_pixmap(matrix=pdf.Matrix(ppi/72,ppi/72)).save(out/f'proposed-{i+1}-{ppi}ppi.png')
    im=Image.open(out/f'proposed-{i+1}-72ppi.png');x=(i%3)*432;y=(i//3)*546+20;sheet.paste(im,(x,y));draw.text((x,y-17),f'{i+1} / {labels[i]}',fill='black')
    current[n-1].get_pixmap(matrix=pdf.Matrix(2,2)).save(out/f'current-{i+1}-144ppi.png')
    old.insert_pdf(current,from_page=n-1,to_page=n-1)
    refdoc=pdf.open(P/'references'/ref)
    for document,cols in [(two,2),(boards,3)]:
        board=document.new_page(width=cols*450+18,height=564)
        titles=[f'CURRENT / PDF {n}',f'PROPOSED / study {i+1}']
        sources=[(current,n-1),(study,i)]
        if cols==3:titles.append(f'{ref} / PDF {rn}');sources.append((refdoc,rn-1))
        for k,(title,(source,pagenum)) in enumerate(zip(titles,sources)):
            x=18+k*450
            board.insert_text((x,16),title,fontsize=9)
            # Current/proposed displayed at actual trim size. SE reference fits
            # proportionally in the same frame, because its scan is larger.
            board.show_pdf_page(pdf.Rect(x,28,x+432,550),source,pagenum)
    refdoc[rn-1].get_pixmap().save(out/f'reference-{i+1}.png')
    refdoc.close()
sheet.save(out/'contact.png')
boards.save(D/'current-proposed-reference.pdf',deflate=True)
two.save(D/'current-versus-proposed.pdf',deflate=True)
old.save(D/'current-six-pages.pdf',deflate=True)
spreads=pdf.open()
for left,right in [(None,0),(1,2),(3,4),(5,None)]:
    q=spreads.new_page(width=864,height=522)
    if left is not None:q.show_pdf_page(pdf.Rect(0,0,432,522),study,left)
    if right is not None:q.show_pdf_page(pdf.Rect(432,0,864,522),study,right)
spreads.save(D/'facing-page-study.pdf',deflate=True)
# Quantify letterfit/leading trials using real rendered baselines, not em names.
tests=pdf.open(D/'type-tests.pdf');assert len(tests)==1
tests[0].get_pixmap(matrix=pdf.Matrix(2,2)).save(out/'type-tests.png')
lines=[l for b in tests[0].get_text('dict')['blocks'] for l in b.get('lines',[])]
headers=[l for l in lines if any(x in ''.join(s['text'] for s in l['spans']) for x in ['Current:',' / natural width'])]
metrics=[]
for i,h in enumerate(headers):
    y=h['bbox'][3];end=headers[i+1]['bbox'][1] if i+1<len(headers) else 500
    body=[l for l in lines if l['bbox'][1]>=y and l['bbox'][3]<end]
    baselines=[l['spans'][0]['origin'][1] for l in body]
    metrics.append({'trial':''.join(s['text'] for s in h['spans']),'lines':len(body),'baseline_pitch_pt':round(statistics.median([b-a for a,b in zip(baselines,baselines[1:])]),2),'mean_characters_full_lines':round(statistics.mean(len(''.join(s['text'] for s in l['spans'])) for l in body[:-1]),1)})
(D/'typography-measurements.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
summary={'study_pages':6,'trim_pt':[432,522],'all_selected_text_units_present':len(expected),'fonts_embedded':True,'production_source_hashes':'unchanged','text_rectangle_overlap_issues':overlaps,'reference_page_numbers':'physical PDF pages, not printed folios','current_source_pdf_pages':current_pages,'current_pdf_sha256':hashlib.sha256((P/'output/macintosh-piforma-working-proof.pdf').read_bytes()).hexdigest(),'image_method':'unchanged original aspect ratios; screenshot viewport crops existing pixels only','physical_print_review':False}
(D/'validation.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2));print(json.dumps(metrics,indent=2))
