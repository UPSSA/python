'''score=int(input("점수를 입력하세요 : "))

if score>=70:
    print("합격")
else:
    print("불합격")
print("수고하셨습니다")'''

print("컴활필기를합격했는지안했는지알아볼까요??")
com=int(input("컴퓨터일반 점수 입력 : "))
excel=int(input("스프레드시트 점수 입력 : "))

if ((com+excel)/2)<60 or com<40 or excel<40:
    print("불합격")
    if ((com+excel)/2)<60:
        print("평균미달이다ㅋ")
    else:
        print("니 과락 수고")
else:
    print("합격")

'''if ((com+excel)/2)>=60 and com>=40 and excel>=40:
    print("합격!")
else:
    print("불합격이야")'''


'''if ((com+excel)/2)<60 or com<40 or excel<40:
    print("불합격")
else:
    print("합격")'''

'''if ((com+excel)/2)>=60 and com>=40 and excel>=40:
    print("합격!")
else:
    print("불합격")
    if com<40 or excel<40:
        print("니 과락 수고")
    else:
        print("평균미달이다ㅋ")'''
