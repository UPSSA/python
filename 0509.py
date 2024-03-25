#poem='''이렇게 정다운
#너 하나 나 하나는
#어디서 무엇이 되어
#다시 만나랴.'''

'''print(poem)

print("이렇게 정다운", end=" ")
print("너 하나 나 하나는", end=" ")
print("어디서 무엇이 되어", end=" ")
print("다시 만나랴", end=" ")'''







print("소금물의 농도를 구하는 프로그램입니다")
salt=int(input("소금물의 양은 몇 g입니까?"))
water=int(input("물의 양은 몇 g입니까?"))

density=salt/(salt+water)*100

print("소금물의 농도: "+str(density)+"%")
