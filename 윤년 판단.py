year=int(input("연도를 입력하시오: "))
a=year%4!=0 and year%100==0
b=year%100!=0 and year%4==0
c=year%400==0

if a or b or c:
    print(year,"년은 윤년입니다.")
else:
    print(year,"년은 평년입니다.")
