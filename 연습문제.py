'''x=int(input("x: "))
y=int(input("y: "))
print("두 수의 합:",x+y)
print("두 수의 차:",x-y)
print("두 수의 곱:",x*y)
print("두 수의 평균:",(x+y)/2)
print("큰 수:",max(x,y))
print("작은 수:",min(x,y))'''


'''r=float(input("r:"))
h=float(input("h:"))
v=3.141592*r**2*h
print("원기둥의 부피:",v)'''



'''num=input("정수를 입력하시오: ")
num1=int(num[:1])
num2=int(num[1:2:1])
num3=int(num[2:3:1])
num4=int(num[3:4:1])
print("자릿수의 합:",num1+num2+num3+num4)'''


'''kg=int(input("물체의 무게를 입력하시오(킬로그램): "))
ms=int(input("물체의 속도를 입력하시오(미터/초): "))
print("물체는",0.5*kg*ms**2,"(줄)의 에너지를 가지고 있습니다.")'''

x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
a=((x1-x2)**2+(y1-y2)**2)**0.5

import turtle as t
t.shape("turtle")

t.goto(x1,y1)
t.goto(x2,y2)
#t.write("점의 길이="+str(a))


'''num=int(input("정수를 입력하시오: "))
s=0
while num>0:
    s+=num%10
    num//=10

print(s)'''

'''a=1234
sum=0
for i in range(4):
    sum+=a%10
    a//=10

print("합계는~~",sum)'''

'''a=input("정수를 입력하시오: ")
sum=0
for i in range(len(a)):
    a=int(a)
    sum+=a%10
    a//=10

print("합계는~~",sum)'''
