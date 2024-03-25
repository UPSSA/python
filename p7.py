def r_f():
    r1=open("d:\\30717 조민선\p7.txt","r")
    for i in r1:
        print(i.rstrip())
    r1.close()

def s_f():
    name=input("누구의 전화번호가 궁금하신가요? ")
    r1=open("d:\\30717 조민선\p7.txt","r")
    for i in r1:
        if name in i:
            print(i.split()[1])
    r1.close()

def a_f():
    f1=open("d:\\30717 조민선\p7.txt","a")

    name=input("추가할 이름 입력 >>> ")
    tell=input("추가할 전화번호 입력 >>> ")

    f1.write(name+" "+tell+"\n")
    f1.close()

def d_f():
    f2=open("d:\\30717 조민선\p7.txt","r")
    data=f2.readlines()
    name=input("삭제할 이름 입력 >>> ")

    for i in data:
        if name in i:
            data.remove(i)

    #print(data)

    f2.close()

    f3=open("d:\\30717 조민선\p7.txt","w")
    for j in data:
        f3.write(j)

    f3.close()

while True:
    print("전화번호부\n")
    print("1:출력 2:검색 3:추가 4:삭제 5:종료\n")
    num=int(input("번호선택 >>> "))

    if num==1:
        r_f()
    elif num==2:
        s_f()
    elif num==3:
        a_f()
    elif num==4:
        d_f()
    elif num==5:
        break
    else:
        print("1부터 5까지 숫자가 아닙니다.")
    print()
