'''import turtle
t=turtle.Turtle()
s=turtle.Screen()
t.shape("turtle")
s.bgcolor("pink")'''

'''import turtle as t
s=t.Screen()
t.shape("turtle")
s.bgcolor("pink")'''

from turtle import *
t=Turtle()
t.shape("turtle")
s=Screen()
s.bgcolor("pink")
name=s.textinput("name box","이름을 입력하시오:")

for i in range(4):
    t.left(90)
    t.fd(100)

t.color("red")
t.write("안녕하세요? "+name+"씨, 터틀 인사드립니다.", font=('Arial',10,'italic'))
