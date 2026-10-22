from PIL import Image, ImageDraw
N=64
im=Image.new('RGBA',(N,N),(0,0,0,0)); d=ImageDraw.Draw(im)
K=(20,16,40,255)
# drop shadow
d.rounded_rectangle((5,7,62,61),radius=7,fill=(40,30,90,110))
# case
d.rounded_rectangle((2,3,59,58),radius=7,fill=(255,240,200,255),outline=K,width=2)
# highlight and shade bands
d.line((7,5,53,5),fill=(255,255,240,255)); d.line((4,9,4,52),fill=(255,255,240,255))
d.line((8,56,53,56),fill=(222,196,140,255)); d.line((57,9,57,52),fill=(222,196,140,255))
d.line((8,55,52,55),fill=(240,220,170,255))
# bezel recess
d.rounded_rectangle((9,8,52,43),radius=3,fill=(70,60,95,255),outline=K,width=1)
# screen
d.rectangle((12,11,49,40),fill=(70,110,255,255))
for y in range(11,41,2): d.line((12,y,49,y),fill=(80,122,255,255))
# menu bar
d.rectangle((12,11,49,13),fill=(255,255,255,255)); d.line((12,14,49,14),fill=K)
d.point((14,12),fill=(255,60,80,255))
for x0,x1 in ((17,19),(22,24),(27,29),(44,47)): d.line((x0,12,x1,12),fill=K)
# AtEase window with folder tab
d.rectangle((16,16,26,18),fill=(255,250,170,255),outline=K)
d.rectangle((15,18,46,38),fill=(255,250,170,255),outline=K)
d.line((16,19,45,19),fill=(255,255,230,255))
cols=[(0,190,255),(255,70,90),(255,190,0),(80,220,90),(190,90,255),(255,120,40),(0,210,190),(255,90,200)]
k=0
for r,y in enumerate((21,29)):
  for c,x in enumerate((18,25,32,39)):
    col=cols[k%len(cols)]+(255,); k+=1
    d.rectangle((x,y,x+5,y+5),fill=col,outline=K)
    d.point((x+1,y+1),fill=(255,255,255,255))
# cursor
for i,(a,b) in enumerate([(0,0),(0,1),(1,1),(0,2),(1,2),(2,2),(0,3),(1,3),(0,4)]): pass
arrow=["K....","KK...","KWK..","KWWK.","KWWWK","KWKK.","KK.K.","K..."]
for j,row in enumerate(arrow):
  for i,ch in enumerate(row):
    if ch=='K': d.point((43+i,33+j),fill=K)
    if ch=='W': d.point((43+i,33+j),fill=(255,255,255,255))
# glass glint
d.line((44,13,48,17),fill=(200,220,255,255)) if False else None

# rainbow apple
ap=[(255,255,255,0)]
stripes=[(97,200,70),(255,200,0),(255,130,20),(240,50,60),(170,60,190),(0,160,240)]
ax,ay=8,46
d.point((ax+3,ay),fill=stripes[0]+(255,)); d.point((ax+4,ay-1),fill=stripes[0]+(255,))
rows=[(1,5),(0,6),(0,5),(0,5),(0,6),(1,5)]
for i,(a,b) in enumerate(rows):
  d.line((ax+a,ay+1+i,ax+b,ay+1+i),fill=stripes[i]+(255,))
d.point((ax+6,ay+3),fill=(255,240,200,255)); d.point((ax+6,ay+4),fill=(255,240,200,255))
d.point((ax+3,ay+1),fill=(255,240,200,255))
# power LED with glow
d.rectangle((49,47,50,51),fill=(60,255,90,255),outline=None)
d.point((48,49),fill=(180,255,190,255)); d.point((51,49),fill=(180,255,190,255))
im.save('piforma-cartoon-64.png')
