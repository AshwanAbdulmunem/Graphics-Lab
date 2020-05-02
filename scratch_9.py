import turtle
colors = ['red','purple','blue','green','yellow']
t = turtle.Turtle()
t.pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%5])
    t.width(x/100+1)
    t.fd(x)
    t.left(59)


