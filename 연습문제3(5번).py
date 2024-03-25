import turtle

import math

s=turtle.Screen()

t1=turtle.Turtle()
t2=turtle.Turtle()

'''x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))'''

x1,y1=0,0
x2,y2=100,100

s.bgcolor("skyblue")
#s.setup(400,400)
#dis=((x1-x2)**2+(y1-y2)**2)**0.5
dis=math.sqrt(math.pow((x2-x1),2)+(y2-y1)**2)

t1.fd(100)
t1.lt(90)
t1.fd(100)
t2.color("red")
t2.shape("turtle")
t2.setheading(45)
t2.fd(dis)
t2.write("점의 길이="+str(dis),font=("arial",20))

'''import turtle as t
t.shape("turtle")

t.goto(x1,y1)
t.goto(x2,y2)'''
