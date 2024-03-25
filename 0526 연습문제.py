'''age=20
if age<20:
    print("20살 미만")
else:
    print("20살 이상")'''

'''age=20
if age<20:
    print("20살 미만")
elif age>=30 and age<=50:
    print("30살 이상 50살 이하")
else:
    print("20살 이상 30살 미만")'''

'''num=int(input("성적을 입력하시오: "))

if num>=90:
    print("A학점입니다.")
elif num>=80:
    print("B학점입니다.")
elif num>=70:
    print("C학점입니다.")
elif num>=60:
    print("D학점입니다.")
else:
    print("F학점입니다.")'''

'''n=int(input("현재 온도를 입력하세요: "))

if n>=25:
    print("반바지를 추천합니다.")
else:
    print("긴바지를 추천합니다.")'''

'''import random
x=random.randint(1,100)
y=random.randint(1,100)
z=x-y

x1=int(input(str(x)+"-"+str(y)+" = "))

if z==x1:
    print("맞았습니다")'''

'''n=int(input("점수를 입력하시오: "))

if n%2==0 and n%3==0:
    print("2와 3으로 나누어떨어집니다.")'''


import random
x=random.randint(0,99)

a=int(input("복권번호를 입력하세요(0~99 사이) : "))
print("당첨번호는 ",x,"입니다.",sep="")


n10=x//10
n1=x%10

a10=a//10
a1=a%10

if n10==a10 and n1==a1:
    print("상금은 100만 원입니다.")
elif n10==a10 or n10==a1 or n1==a10 or n1==a1:
    print("상금은 50만원 원입니다.")
else:
    print("상금xx")


















