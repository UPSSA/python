print("♥여행 준비 환전프로그램♥")
moneys=[100,50,20,10,2,1]
won=int(input("환전할 돈을 입력하세요 : "))
rate=int(input("1달러 당 환율을 입력하세요 : "))
doller=won//rate
remain=won%rate

print(doller,"달러",remain,"원")

x=doller
y=0

for i in moneys:
    y=x//i
    x=x%i
    print( "%3d 달러 : %1d개" %(i,y))
