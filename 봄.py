'''m=8

if m>=3 and m<=5:
    print("봄이네요~!")
else:
    print("봄이 아니네요 그렇다면..?")'''



'''m=8

if m==3 or m==4 or m==5:
    print("봄이네요~!")
else:
    print("봄이 아니네요 그렇다면..?")'''



m=int(input("월 입력: "))

if 3<=m<=5:
    print("봄이네요~!")
elif 6<=m<=8:
    print("봄이 아니네요 그렇다면..? 여름이네요")
elif 9<=m<=11:
    print("가을이네ㅋㅋ")
else:
    print("하 겨울이네..")
