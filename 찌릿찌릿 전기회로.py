num1=input("1번 전지가 있습니까? (Y/N)")
num2=input("2번 전지가 있습니까? (Y/N)")

num1=num1.upper()
num2=num2.upper()

if num1=="Y" and num2=="Y":
    print("직렬연결 : 전구에 불이 켜집니다.")
    print("병렬연결 : 전구에 불이 켜집니다.")
elif num1=="Y" or num2=="Y":
    print("직렬연결 : 전구에 불이 꺼집니다.")
    print("병렬연결 : 전구에 불이 켜집니다.")
else:
    print("직렬연결 : 전구에 불이 꺼집니다.")
    print("병렬연결 : 전구에 불이 꺼집니다.")

