import turtle as t
t.shape("turtle")
t.pensize(2)
t.pencolor("#ff3a3a")

for i in range(5) :
    t.fd(100)
    t.lt(72)

t.penup()
t.pencolor("#000000")
t.goto(-300,100)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(80)
t.end_fill()
