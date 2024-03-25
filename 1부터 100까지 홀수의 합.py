#1부터 100까지 홀수의 합

a=1
sum1=0

while a<=100:
    sum1+=a
    a+=2
print("1부터 100까지 홀수의 합은",sum1,"입니다.")


sum2=0
for i in range(1,101,2):
    sum2+=i
print("1부터 100까지 홀수의 합은",sum2,"입니다.")
