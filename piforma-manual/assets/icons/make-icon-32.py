from PIL import Image
import sys
out=sys.argv[1] if len(sys.argv)>1 else 'piforma-icon-32.png'
C=dict(K=(0,0,0),H=(250,248,236),B=(224,219,199),b=(190,184,163),d=(140,135,118),
 r1=(60,60,64),r2=(95,95,100),r3=(135,135,140),s=(112,112,220),t=(96,96,200),
 M=(255,255,255),w=(221,221,221),W=(250,250,250),g=(120,120,120),L=(60,230,80),m=(90,90,90),
 ag=(97,187,70),ay=(253,184,39),ao=(245,130,31),ar=(224,58,62),ap=(150,61,151),ab=(0,157,220),
 i1=(60,150,230),i2=(230,80,60),i3=(240,200,60),i4=(80,180,90),i5=(150,90,170))
im=Image.new('RGBA',(32,32),(0,0,0,0)); px=im.load()
def P(x,y,c): px[x,y]=C[c]+(255,)
def R(x0,y0,x1,y1,c):
  for y in range(y0,y1+1):
    for x in range(x0,x1+1): P(x,y,c)
# body: x1..30, y2..29, corners cut 2px
X0,Y0,X1,Y1=1,1,30,30
R(X0,Y0,X1,Y1,'B')
for (cx,cy,dx,dy) in [(X0,Y0,1,1),(X1,Y0,-1,1),(X0,Y1,1,-1),(X1,Y1,-1,-1)]:
  for (a,b_) in [(0,0),(1,0),(0,1)]: px[cx+a*dx,cy+b_*dy]=(0,0,0,0)
# outline
for x in range(X0+2,X1-1): P(x,Y0,'K'); P(x,Y1,'K')
for y in range(Y0+2,Y1-1): P(X0,y,'K'); P(X1,y,'K')
for (x,y) in [(X0+1,Y0+1),(X1-1,Y0+1),(X0+1,Y1-1),(X1-1,Y1-1)]: P(x,y,'K')
# highlight top/left, shade bottom/right
for x in range(X0+2,X1-1): P(x,Y0+1,'H')
for y in range(Y0+2,Y1-1): P(X0+1,y,'H')
for x in range(X0+2,X1-1): P(x,Y1-1,'d')
for y in range(Y0+2,Y1-1): P(X1-1,y,'d')
P(X0+1,Y1-2,'b'); P(X1-1,Y0+2,'b')
for x in range(X0+3,X1-2): P(x,Y1-2,'b')
for y in range(Y0+3,Y1-2): P(X1-2,y,'b')
# recess x5..26, y5..22: shadow top/left (dark), lighter bottom/right
RX0,RY0,RX1,RY1=5,4,26,20
R(RX0,RY0,RX1,RY1,'r2')
for x in range(RX0,RX1+1): P(x,RY0,'d')
for y in range(RY0,RY1+1): P(RX0,y,'d')
for x in range(RX0+1,RX1+1): P(x,RY1,'H')
for y in range(RY0+1,RY1+1): P(RX1,y,'H')
for x in range(RX0+1,RX1): P(x,RY0+1,'r1')
for y in range(RY0+1,RY1): P(RX0+1,y,'r1')
for x in range(RX0+2,RX1): P(x,RY1-1,'r3')
for y in range(RY0+2,RY1): P(RX1-1,y,'r3')
# screen x7..24 y7..20
SX0,SY0,SX1,SY1=7,6,24,18
R(SX0,SY0,SX1,SY1,'s')
for y in range(SY0+1,SY1+1):
  for x in range(SX0,SX1+1):
    if (x*3+y*5)%7==0: P(x,y,'t')
R(SX0,SY0,SX1,SY0,'M')
for x in (10,11,13,14,16,17,22,23): P(x,SY0,'m')
P(8,SY0,'K')
# AtEase window with a tab, x9..22 y8..18
R(10,7,14,7,'w'); P(9,7,'g') if False else None
for x in range(10,15): P(x,7,'w')
R(9,8,22,18,'w')
for x in range(9,23): P(x,8,'g'); P(x,18,'g')
for y in range(8,19): P(9,y,'g'); P(22,y,'g')
for x in range(10,15): P(x,8,'w')
for x in (10,14): P(x,7,'g')
for x in range(11,14): P(x,7,'w')
cols=[11,14,17,20]
icn=[['i1','i4','i3','i2'],['i4','i5','g','i2'],['g','i1','g','i3']]
for ri,y in enumerate([10,13]):
  for ci,x in enumerate(cols): R(x,y,x+1,y+1,icn[ri][ci])
for ci,x in enumerate(cols): R(x,16,x+1,16,icn[2][ci])
apple=[(22,'ag',[5]),(23,'ag',[4,6]),(24,'ay',[4,5,6]),(25,'ar',[4,5]),(26,'ap',[4,5,6]),(27,'ab',[4,6])]
for y,c,xs in apple:
  for x in xs: P(x,y,c)
# LED
P(25,23,'L'); P(25,24,'L')
im.save(out)
