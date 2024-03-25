#연산자의 우선순위와 종류
#연산자는 산술, 관계, 논리, 비트 연산자가 있다
#1.()[]{}
#2.**
#3.+ - ~
#4.* / % //
#5.+ -
#6.<< >>
#7.&
#8.^
#9.|
#10.< <= > >=
#11.== !=
#12.= %= /= //= += -= *= **=
#13.not
#14.and
#15.or
#16.if~else

#산술 연산자
print("-------- 산술 연산자 --------")
print("a = 7, b = 3일 때")

p_a=7
p_b=3
print("a의 값: ",p_a) #대입
print("b의 값: ",p_b) #대입

print("a + b의 결과 값: ",p_a+p_b) #덧셈

print("a - b의 결과 값: ",p_a-p_b) #뺄셈

print("a * b의 결과 값: ",p_a*p_b) #곱셈

print("a / b의 결과 값: ",p_a/p_b) #나눗셈

print("a // b의 결과 값: ",p_a//p_b) #몫만 구하는 나눗셈

print("a % b의 결과 값: ",p_a%p_b) #나머지만 구하는 나눗셈

print("a ** b의 결과 값: ",p_a**p_b) #제곱

print("\n-------- 대입 연산자 --------")
print("a = 10 일 때")

p_a=10
print("a의 결과 값: ",p_a) #대입

p_a+=5
print("a += 5의 결과 값: ",p_a) #덧셈 후 대입

p_a-=5
print("a -= 5의 결과 값: ",p_a) #뺄셈 후 대입

p_a*=5
print("a *= 5의 결과 값: ",p_a) #곱셈 후 대입

p_a/=5
print("a /= 5의 결과 값: ",p_a) #나눗셈 후 대입

p_a//=5
print("a //= 5의 결과 값: ",p_a) #몫을 구한 후 대입

p_a%=5
print("a %= 5의 결과 값: ",p_a) #나머지를 구한 후 대입

p_a**=5
print("a **= 5의 결과 값: ",p_a) #제곱을 구한 후 대입

print("\n-------- 관계 연산자 --------")
print("a = 10, b = 20일 때")

p_a=10
p_b=20
print("a == b의 결과 값: ",p_a==p_b) #같음

print("a != b의 결과 값: ",p_a!=p_b) #같지 않음

print("a > b의 결과 값: ",p_a>p_b) #큼

print("a < b의 결과 값: ",p_a<p_b) #작음

print("a >= b의 결과 값: ",p_a>=p_b) #크거나 같음

print("a <= b의 결과 값: ",p_a<=p_b) #작거나 같음

print("\n-------- 논리 연산자 --------")
print("a = 10, b = 20일 때")

print("(a == b) and (a < b)의 결과 값: ",(p_a==p_b)and(p_a<p_b)) #그리고

print("(a == b) or (a < b)의 결과 값: ",(p_a==p_b)or(p_a<p_b)) #또는

print("not (a < b)의 결과 값: ",not(p_a<p_b)) #부정

print("\n-------- 비트 연산자 --------")
print("a = 3, b = 2일 때")
p_a=3
p_b=2

print("a & b의 결과 값: ",(p_a&p_b)) #비트 논리곱

print("a | b의 결과 값: ",(p_a|p_b)) #비트 논리합

print("a ^ b의 결과 값: ",(p_a^p_b)) #비트 배타적 논리합

print("~ a의 결과 값: ",(~p_a)) #비트 부정


print("a = 23일 때")
p_a=23
print("a << b의 결과 값: ",(p_a<<p_b)) #비트 왼쪽 시프트

print("a >> b의 결과 값: ",(p_a>>p_b)) #비트 오른쪽 시프트

