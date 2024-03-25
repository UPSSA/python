def dis(a1,b1,c1,d1):
    return(((c1-a1)**2+(d1-b1)**2)**(1/2))

x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))

a=dis(x1,y1,x2,y2)
print("두 지점 사이의 거리=",a)
