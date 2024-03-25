import turtle as t
import random
t.shape("turtle")
t.speed(200)

def dc():
    r=random.randint(20,100)
    for i in range(6):
        t.circle(r)
        t.left(60)

def dc_r(r):
    for i in range(10):
        t.circle(r)
        t.left(60)

for i in range(3):
    r=random.randint(20,100)
    dc_r(r)

'''for i in range(20):
    dc()'''

    

