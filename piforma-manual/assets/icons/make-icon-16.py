from PIL import Image
import re
# Reuse the palette from the 32-pixel icon.
exec(re.sub(r'(?m)^out=.*$','',open('make-icon-32.py').read().split('im=Image.new')[0]))
im=Image.new('RGBA',(16,16),(0,0,0,0)); px=im.load()
def P(x,y,c): px[x,y]=C[c]+(255,)
def R(x0,y0,x1,y1,c):
  for y in range(y0,y1+1):
    for x in range(x0,x1+1): P(x,y,c)
R(1,1,14,15,'B'); R(0,2,15,14,'B')
for x in range(1,15): P(x,0,'K'); P(x,15,'K')
for y in range(1,15): P(0,y,'K'); P(15,y,'K')
for x in range(1,15): P(x,1,'H')
for y in range(1,15): P(1,y,'H')
for x in range(2,15): P(x,14,'d')
for y in range(2,15): P(14,y,'d')
P(1,14,'b'); P(14,1,'b')
# recess x3..12 y3..10
R(3,3,12,10,'r2')
for x in range(3,13): P(x,3,'d')
for y in range(3,11): P(3,y,'d')
for x in range(4,13): P(x,10,'H')
for y in range(4,11): P(12,y,'H')
# screen x4..11 y4..9
R(4,4,11,9,'s'); R(4,4,11,4,'M')
for x in (6,7,9): P(x,4,'m')
P(4,5,'s'); R(5,6,10,9,'w')
for x in range(5,11): P(x,6,'g')
P(6,8,'i1'); P(8,8,'i4'); P(10,8,'i2') if False else P(9,8,'i2')
for y in range(6,10): P(5,y,'g'); P(10,y,'g')
# apple and LED
P(3,11,'ag'); P(2,12,'ay'); P(3,12,'ay'); P(2,13,'ar'); P(3,13,'ap')
P(12,12,'L')
im.save('piforma-icon-16.png')
