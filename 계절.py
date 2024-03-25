spring=[3,4,5]
summer=[6,7,8]
autumn=[9,10,11]
winter=[12,1,2]

m=int(input("계절이 알고 싶다면 당신이 현재 몇월을 살고 있는지 말해봐~^^: "))

if m in spring:
    print("봄이란다.....")
elif m in summer:
    print("여름이구나.......")
elif m in autumn:
    print("가을입니다")
elif m in winter:
    print("겨울이다~")
else:
    print("엥.... 다시 입력하세요")
