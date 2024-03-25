def f_to_c(f1):
    #화씨를 섭씨로 바꾸기
    return (f1-32)*5/9

f=int(input("화씨온도: "))
c=f_to_c(f)
print("섭씨온도",c)
