price=int(input("투입한 돈: "))
pay=int(input("물건가격: "))
change=price-pay
print("거스름돈:",change)

print("500원 동전의 개수:",change//500)
print("100원 동전의 개수:",(change%500)//100)
print("50원 동전의 개수:",(change%500)%100//50)
