import turtle

myTurtle = turtle.Turtle(shape="turtle")
myTurtle.pensize(20)
myTurtle.circle(50)
print(myTurtle.position())
myTurtle.pencolor("blue")

myTurtle.penup()
myTurtle.setposition(-120, 0)
print(myTurtle.position())
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.pencolor("green")
myTurtle.penup()
myTurtle.setposition(60, 60)
print(myTurtle.position())
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.pencolor("yellow")
myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.pencolor("red")
myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)

turtle.done()