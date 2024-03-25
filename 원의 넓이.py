r=10
pi=3.141592
#print("반지름이", r,"인 원의 넓이", r**2*pi)

'''r+=10
print("반지름이", r,"인 원의 넓이", r**2*pi)
r+=10
print("반지름이", r,"인 원의 넓이", r**2*pi)'''

'''for i in range(5):
    print("반지름이", r,"인 원의 넓이", r**2*pi)
    r+=10'''

'''for i in range(5):
    print("반지름이", r,"인 원의 넓이", round(r**2*pi,2))
    r+=10'''

'''for i in range(5):
    print("반지름이", r,"인 원의 넓이", round(r**2*pi))
    r+=10'''

for i in range(10,60,10):
    print("반지름이", i,"인 원의 넓이", round(i**2*pi))
