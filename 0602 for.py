'''for i in range(5):
    print("★", end="")'''

for a in range(5):
    for i in range(5):
        print("★", end="")
    print("\n")

'''for e in range(4):
    for u in range(3):
        print("♥", end="")
    print("\n")'''

'''for e in range(7):
    for u in range(7):
        print("♥", end="")
    print("\n")'''

'''for e in range(7):
    for u in range(e+1):
        print("♥", end="")
    print("\n")'''

for e in range(7):
    for u in range(7-e):
        print("♥", end="")
    print("\n")
