import turtle

r=int(input("원의 반지름을 입력하시오:"))
color=input("원의 색깔을 입력하시오:")

c=turtle.Turtle()
c.shape("turtle")

c.fillcolor(color)
c.begin_fill()

c.color(color)
c.circle(r)

c.end_fill()

