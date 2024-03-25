import turtle
side=int(input("한 변의 길이 입력:"))
angle=int(input("몇 각형을 그릴 거야?:"))
t=turtle.Turtle()

'''for j in range(6):
    for i in range(3):
        t.forward(side)
        t.left(120)
    t.left(60)'''

for i in range(angle):
    t.forward(side)
    t.left(360/angle)
