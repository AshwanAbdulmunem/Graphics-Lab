import turtle
ob = turtle.Turtle()
ob.getscreen().bgcolor("red")
ob.up()
ob.goto(0, -100)
ob.down()

ob.begin_fill()
ob.fillcolor("yellow")
ob.circle(100)
ob.end_fill()

ob.up()
ob.goto(-67, -40)
ob.setheading(-60)
ob.width(5)
ob.down()
ob.circle(80, 120)
ob.fillcolor("black")

for i in range(-35, 105, 70):
    ob.up()
    ob.goto(i, 35)
    ob.setheading(0)
    ob.down()
    ob.begin_fill()
    ob.circle(10)
    ob.end_fill()

ob.hideturtle()
