#생년월일 여덟자리를 입력받아서 나이를 출력하는 프로그램입니다.
name=input("당신의 이름은 무엇입니까? ")
birthday=input("생년월일을 8자리(yyyymmdd)로 입력해주세요. ")
today=input("오늘의 날짜를 8자리(yyyymmdd)로 입력해주세요. ")

t_year=int(today[:4])
t_month=int(today[4:6:1])
t_day=int(today[6:8:1])

year=int(birthday[:4])
month=int(birthday[4:6:1])
day=int(birthday[6:8:1])
age=2023-int(year)

print("\n오늘은 "+str(t_year)+"년 "+str(t_month)+"월 "+str(t_day)+"일이군요!")
print(name+"님은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일에 태어났군요!")


'''if t_month>=month and t_day>=day:#(생일이 지났다면)
    age=2023-year
    print("올해 만 나이는",str(age)+"살이군요!")

else:
    age=(2023-year)-1
    print("올해 만 나이는",str(age)+"살이군요!")'''

'''if t_month<month or t_day<day:#(생일이 지나지 않았다면)
    age=(2023-year)-1
    print("올해 만 나이는",str(age)+"살이군요!")

else:
    age=2023-year
    print("올해 만 나이는",str(age)+"살이군요!")'''


if not(t_month>=month and t_day>=day):#(생일이 안 지났다면)
    age=2023-year-1
    print("올해 만 나이는",str(age)+"살이군요!")

else:
    age=(2023-year)
    print("올해 만 나이는",str(age)+"살이군요!")

