import time

'''thisyear
age

a=(2050-thisyear)+age

s=time.time()
s=int(s)
m=s//60
h=m//60
day=h//24
year=day//365

year+=1970'''

thisyear=int(time.time())//(60*60*24*365)+1970

print("올해는 %d년입니다." %thisyear)
age=int(input("당신의 나이를 입력하세요 : "))
year=int(input("몇 년도에 나이가 궁금하세요? : "))
age1=(year-thisyear)+age
print("%d년에는 %d살이군요." %(year,age1))
