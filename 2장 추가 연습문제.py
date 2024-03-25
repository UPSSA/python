'''name=input("이름을 입력하시오 : ")
age=int(input("나이를 입력하시오 : "))
x=100-age
print(name+"씨는 "+str(2020+x)+"년에 100살이시네요!")'''

'''r=int(input("반지름을 입력하시오 : "))
pi=3.141592
area=r*r*pi
print("반지름이 {0} 인 원의 넓이 = {1}".format(r, area))'''



#side=int(input("side 입력 : "))




'''import turtle as t
t.shape("turtle")

for i in range(3):
    t.fd(200)
    t.left(120)'''




import turtle as t
t.shape("turtle")

side=100
angle=90

for j in range(4):
    for i in range(4):
        t.fd(side)
        t.left(angle)
    t.left(angle)

t.right(90)





    
'''for i in range(4):
    t.fd(side)
    t.left(angle)

t.left(angle)

for i in range(4):
    t.fd(side)
    t.left(angle)

t. left(angle)

for i in range(4):
    t.fd(side)
    t.left(angle)'''
