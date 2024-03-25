def p_100():
    j=1
    sum2=0
    while j<=100:
        sum2+=j
        j+=1
    print("1부터 100까지의 합은",sum2,"입니다.")

def f_10():
    fac=1
    for i in range(1,11):
        fac*=i

    print("1부터 10까지의 팩토리얼은",fac,"입니다.")    

#f_10()
#p_100()
