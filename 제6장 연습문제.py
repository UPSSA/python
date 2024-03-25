#1번
'''for i in range(1,101):
    if i%2==0:
        print(i, end=" ")'''

#2번
'''for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)'''

#3번
'''import turtle
t=turtle.Turtle()
t.color("orange")

for i in range(1,10):
    for j in range(1,6):
        t.left(144)
        t.fd(200)
    t.left(10)'''



#4번
'''import turtle
import random
t=turtle.Turtle()
t.shape("turtle")
t.speed(100)

for i in range(10):
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    r=random.randint(1,100)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.circle(r)'''

#5번
'''n=1234
sum=0
while n>0:
    digit=n%10 #1234를 10으로 나눈 나머지
    sum=sum+digit#sum이라는 변수에 나머지를 저장
    n=n//10 #n이라는 변수에 1234를 10으로 나눈 몫을 저장
print(sum)
#1234, 123, 12, 1 순서대로 나누어짐'''

#6번
'''year=0
balance=1000
while balance<=2000:
    year=year+1
    interest=balance*0.07
    balance=balance+interest
print(year,"년이 걸립니다.")'''

#7번
'''import turtle
t=turtle.Turtle()
t.shape("turtle")

for i in range(5):
    t.fd(100)
    t.right(90)
    t.fd(10)
    t.right(90)
    t.fd(100)
    t.left(90)
    t.fd(10)
    t.left(90)'''

#8번
'''a=int(input("3*9 = "))
while a!=3*9:
    a=int(input("3*9 = "))
print("맞았습니다.")'''

#9번
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("red","yellow")
t.begin_fill()
while True:
    t.fd(200)
    t.left(170)
    if abs(t.pos())<1:
        break
t.end_fill()
