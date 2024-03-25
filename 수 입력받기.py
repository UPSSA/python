'''x=300
y=400'''

x=int(input("첫번째 값 입력 : "))
y=float(input("두번째 값 입력 : "))
sum=x+y
print(x,"과",y,"의 합은",sum,"입니다.")
#print(str(x)+"과 "+str(y)+"의 합은 "+str(sum)+"입니다.")

#콤마를 쓰고도 띄어쓰기 안하는 법
#print(x,"과 ",y,"의 합은 ",sum,"입니다." ,sep="")
#sep=""

#print(x,"과 ",y,"의 합은 ",sum,"입니다.",sep="")

print("%d과 %d의 합은 %d입니다." %(x, y, sum))
print("%d과 %f의 합은 %f입니다." %(x, y, sum))
print("%d과 %.1f의 합은 %.1f입니다." %(x, y, sum))
#type("300과 42.5의 합은 342.5입니다.")

print("{1}과 {0}의 합은 {2}입니다.".format(x, y, sum))
