import random

print("~범인 잡기 게임~")

score=50 #점수 초기화

#잡을때까지무한반복
while True:
    room=random.randint(1,5) #범인이 숨은 방

    door=int(input("방 번호를 입력하세요: ")) #경찰이 열 문
    
    #잡았다, 못잡았다, 다른 방문을 열었다
    if room==door:
        print("잡았다!")
        score+=100
        break
    elif door>5:
        print("다른 방문을 열어버렸다~! ㅈㅅㅎㄴㄷ")
    else:
        print("못잡았다 ㅠㅠ~!!! ㅠㅠ!!")
        score-=10
print("~~게임종료~~")
print("당신의 점수는",score,"입니다.")
