import turtle
s=turtle.Screen()
s.setup(600,600)
t=turtle.Turtle()
t.speed(10)
s.bgcolor("black")
col=["yellow","blue","white","green"]
c=0

for i in range (50):
    t.fd(i*10)
    t.rt(144)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=1
        