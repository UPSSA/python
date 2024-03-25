import turtle
t=turtle.Turtle()

'''t.goto(0,-10*0)
t.circle(50+10*0)

t.goto(0,-10*1)
t.circle(50+10*1)

t.goto(0,-10*2)
t.circle(50+10*2)

t.goto(0,-10*3)
t.circle(50+10*3)

t.goto(0,-10*4)
t.circle(50+10*4)

'''

#range(0,7,1)
#range(6,-1,-1)

colors=["red","orange","yellow","green","blue","navy","purple"]
#colors=["purple","navy","blue","green","yellow","orange","red"]
t.speed(100)
for i in range(6,-1,-1):
    t.fillcolor(colors[i])
    t.penup()
    t.goto(0,-20*i)
    t.pendown()
    t.begin_fill()
    t.circle(50+20*i)
    t.end_fill()
    




'''t.circle(10)
t.circle(20)
t.circle(30)
t.circle(40)
t.circle(50)'''
