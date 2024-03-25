m=int(input("숫자 입력 : "))


for n in range(1,m+1):
    count=0
    n10=n//10
    n1=n%10

    #print("십의 자리 :",n10)
    #print("일의 자리 :",n1)


    if n10 in [3,6,9]:
          #print("짝")
            count+=1

    if n1 in [3,6,9]:
          #print("짝")
            count+=1

    if count==0:
        print("%2d" %(n), end=" ")
    elif count==1:
        print("짝",end=" ")
    else:
        print("짝짝",end=" ")
    if n%10==0:
        print()
