r=int(input("반지름 입력 : "))
pi=3.141592
area=r*r*pi

print("반지름이 "+str(r)+"인 원의 넓이는 "+str(area))
print("반지름이 ",r,"인 원의 넓이는 ",area,sep="")
print("반지름이 %d인 원의 넓이는 %.4f" %(r, area))
print("반지름이 {0}인 원의 넓이는 {1}".format(r, area))

print("반지름이 %d인 원의 넓이는 %.2f" %(r, area))
print("반지름이 %d인 원의 넓이는 %d" %(r, area))
