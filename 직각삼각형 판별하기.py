a=int(input("변a의 길이: "))
b=int(input("변b의 길이: "))
c=int(input("변c의 길이: "))

if c<a+b:
    if (a**2)+(b**2)==(c**2):
        print("직각삼각형 입니다.")
    else:
        print("직각삼각형이 아닙니다.")
