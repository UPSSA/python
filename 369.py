n=int(input("숫자 입력(두자리수까지만가능): "))

for i in range(1,n+1):
    a=i//10
    b=i%10

    #print(i, end=" ")
    if a==3 or a==6 or a==9:
        print("짝", end="")
    else:
        print(a, end="",sep="")
    if b==3 or b==6 or b==9:
        print("짝", end="")
    else:
        print(a, end="",sep="")
    print()
