def r_f():
    r1=open("d:\\30717 조민선\p7.txt","r")
    for i in r1:
        print(i.rstrip())
    r1.close()

def s_f():
    name=input("누구의 전화번호가 궁금하신가요?")
    r1=open("d:\\30717 조민선\p7.txt","r")
    for i in r1:
        if name in i:
            print(i.split()[1])

print("전화번호부")
print("1번 출력, 2번 검색, 3번 추가, 4번 삭제")
num=int(input("뭐할건가요?"))

if num==1:
    r_f()
elif num==2:
    s_f()
elif num==3:
    print("준비중")
else:
    print("준비중")
