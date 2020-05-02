import turtle
a = turtle.Turtle()
a.up()
a.goto(0, -100)
a.down()

a.begin_fill()
a.fillcolor("yellow")
a.circle(100)
a.end_fill()

a.up()
a.goto(-67, -40)
a.setheading(-60)
a.width(5)
a.down()
a.left(58)
a.forward(110)
a.fillcolor("black")

for i in range(-35, 105, 70):
    a.up()
    a.goto(i, 35)
    a.setheading(0)
    a.down()
    a.begin_fill()
    a.circle(10)
    a.end_fill()

a.home()
a.clear()
a.color("red")
def flow():
    for i in range(0,1):
        a.left(60)
        a.forward(100)
        for j in range(0, 17):
            a.forward(10)
            a.left(10)
        a.forward(10)

a.begin_fill()
flow()
a.end_fill()
a.penup()
a.home()
a.pendown()
a.right(150)
def flow1():
    for i in range(0,1):
        a.right(60)
        a.forward(100)
        for j in range(0, 17):
            a.forward(10)
            a.right(10)
        a.forward(10)

a.begin_fill()
flow1()
a.end_fill()
a.home()

turtle.done()