import random

import turtle as t
s=t.Screen()





t.penup()
t.goto(-100,150)
t.write("동전 던지기 게임")
t.goto(0,0)
img1="D://front.gif"
img2="D://back.gif"
s.addshape(img1)
s.addshape(img2)


#print("동전 던지기 게임")

coin=random.randint(0,1)

#print(coin)

if coin==0:
    t.shape(img2)
else:
    t.shape(img1)
