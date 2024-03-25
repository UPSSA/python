'''for 변수 in rage(시작, 끝, 간격):
    반복할명령문
    
초기화
while 끝나는 조건:
    참일때반복할명령문
    간격'''


a=1
sum1=0
while a<=100:
    sum1+=a
    a+=1
print("1부터 100까지의 합은",sum1,"입니다.")


sum2=0
for i in range(1,101,1):
    sum2+=i
print("1부터 100까지의 합은",sum2,"입니다.")
