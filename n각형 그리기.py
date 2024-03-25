def draw():
    n=s.textinput("","몇각형을 원하시나요?")
    n=int(n)

    for i in range(n):
        t.fd(100)
        t.left(360/n)

def draw_c(c):
    n=s.textinput("","몇각형을 원하시나요?")
    n=int(n)
    t.color(c)

    for i in range(n):
        t.fd(100)
        t.left(360/n)

import turtle
t=turtle.Turtle()
t.shape("turtle")
s=turtle.Screen()

#n=int(input("몇각형을 원하시나요?"))

draw()
draw()
draw_c("red")
draw_c("blue")
