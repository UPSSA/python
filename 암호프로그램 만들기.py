'''s=input("말해보렴:")

print("평문 :", s)
print("암호문 :", s[-1::-1])'''




'''r="산토끼 토끼야 어디를 가느냐? 깡총깡총 뛰어서 어디를 가느냐?"

r=r.rstrip("?")

r=r.split()

a=r[3]
a=a.rstrip("?")

r[3]=a

for i in range(len(r)):
    print(r[i][-1::-1],end=" ")'''

rabbit="산토끼 토끼야 어디를 가느냐 깡총깡총 뛰어서 어디를 가느냐"
r=rabbit.split()


for i in r:
    print(i[-1::-1],end=" ")

print()

for i in range(len(r)):
    a=r[i]
    print(a[-1::-1],end=" ")
