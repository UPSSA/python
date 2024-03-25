'''import random

num=random.randint(1,4)
print("주민등록번호의 성별 정보 번호를 생성합니다.")
print("생성번호:",num)

if num%2==0:
    print("여성입니다.")
else:
    print("남성입니다.")'''

num=input("주민번호를 입력하세요 *예)010101-1234567 >> ")
num1=int(num[7])

if num1%2==0:
    print("여성입니다.")
else:
    print("남성입니다.")
