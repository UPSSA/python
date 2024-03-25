import random

import turtle as t
s=t.Screen()

t.penup()
t.goto(-100,150)
t.write("주사위 던지기 게임")
t.goto(0,0)

img1="D://1.gif"
img2="D://2.gif"
img3="D://3.gif"
img4="D://4.gif"
img5="D://5.gif"
img6="D://6.gif"

s.addshape(img1)
s.addshape(img2)
s.addshape(img3)
s.addshape(img4)
s.addshape(img5)
s.addshape(img6)

x=random.randint(1,6)

if x==1:
    t.shape(img1)
elif x==2:
    t.shape(img2)
elif x==3:
    t.shape(img3)
elif x==4:
    t.shape(img4)
elif x==5:
    t.shape(img5)
else:
    t.shape(img6)

