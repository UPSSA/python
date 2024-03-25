import random
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(100)

for i in range(50):
    side=random.randint(30,100)
    angle=random.randint(-180,180)
    r=random.random()
    g=random.random()
    b=random.random()
    t.color(r,g,b)
    t.fd(side)
    t.left(angle)
