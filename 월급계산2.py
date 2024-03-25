print("♥월급 지폐 계산 프로그램♥")
moneys=[50000,10000,5000,1000,500,100]
won=int(input("너의 월급은 얼마니? 입력해보자!: "))

print("너의 월급은 %d이구나!"%(won))

x=won
y=0

for i in moneys:
    y=x//i
    x=x%i
    print( "%5d원 화폐의 개수 : %3d개" %(i,y))
