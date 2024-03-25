import math

import turtle as t
t.shape("turtle")

t.left(45)

x1,y1=0,0
x2,y2=100,100

#d=(x2-x1)**2+(y2-y1)**2
d=math.pow(x2-x1,2)+math.pow(y2-y1,2)
d=math.sqrt(d)

t.fd(d)
