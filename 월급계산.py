salary=int(input("월급을 입력하세요: "))
print("당신의 월급은",salary,"입니다 좀 쩌는데?ㅋ")
tax=salary*0.1
money=int(salary-tax)
print("당신의 월급인줄 알았지? 사실 실수령액은",money)

print("50000원 지폐의 개수:",money//50000)
print("10000원 지폐의 개수:",(money%50000)//10000)
print("5000원 지폐의 개수:",(money%50000)%10000//5000)

'''print("50000원 지폐의 개수:",money//50000)
print("10000원 지폐의 개수:",(money%50000)//10000)
print("5000원 지폐의 개수:",(money%50000)%10000//5000)'''







'''if salary>=300:
    print("한달에 이만큼",salary,"버는구나! 좀 쩌는데?ㅋ")
else:
    print("한달에 겨우",salary,"이거 밖에?")'''
