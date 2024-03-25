#가로200 세로100 사각형 그리기
def square(w,h):
    for i in range(2):
        t.fd(w)
        t.left(90)
        t.fd(h)
        t.left(90)

#한 변의 길이가 200인 삼각형 그리기
def tri(side):
    for i in range(3):
        t.fd(side)
        t.left(120)

#반지름이 100인 원 그리기
def cir(r):
    #t.color("red")
    t.circle(r)



import turtle as t
t.shape("turtle")
s=t.Screen()
f=s.textinput("PYTHON","도형을 입력하시오: ")
print(f)

if f=="직사각형":
    w=int(s.textinput("PYTHON","가로:"))
    h=int(s.textinput("PYTHON","세로:"))
    square(w,h)
elif f=="정삼각형":
    side=int(s.textinput("PYTHON","한 변의 길이:"))
    tri(side)
elif f=="원":
    r=int(s.textinput("PYTHON","반지름의 길이:"))
    cir(r)
else:
    t.write("잘못입력하셧읍니다.")




'''#함수 만들기-인수 x,return x
def 함수이름():
    명령문1
    명령문2'''

'''square()

t.penup()
t.goto(-300,0)
t.pendown()

square()

t.penup()
t.goto(-50,150)
t.pendown()

cir(50)

t.penup()
t.goto(-150,-200)
t.pendown()

tri()'''

'''for i in range(50,201,50):
    cir(i)'''
