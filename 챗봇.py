import random


a=["안녕","반가워요^^","hello","ㅎㅇ","hi","방가방가","니하오~"]
age=["몇살","몇년생","연세","나이"]
song=["노래","음악","뮤직","가수","아티스트"]

total=a+age+song
#print(total)
print("나랑대화하겠니?싫어도해야한단다.빨리나한테인사를하렴")
while True:

    q=input(">>> ")
    if "끝" in q:
        break
    for i in total:
        if i in q and i in a:
            print(random.choice(["반갑다 친구야","하이","오랜만이네요","하지만난집에가고싶어","정말이지너무반갑다~"]))
            break
        elif i in q and i in age:
            print(random.choice(["나는 열아홉살이란다~~~","나는05년생이라서19살이야","19세인데ㅋㅋ","나는고삼이다"]))
            break
        elif i in q and i in song:
            print(random.choice(["내가좋아하는아이돌은~","너아이돌좋아해?나는그게뭔지잘몰라","피곤하다그만얘기하자","난가수별로안좋아해"]))
            break
    else:
        print("무슨헛소리노?")
        break
