import turtle
from time import *
win = turtle.Screen()

t=turtle.Turtle()

t.screen.bgcolor("pink")
t.color("red")
t.goto(40,50)
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()

t.ht()
t.color("red")
t.home()
t.color("red")
t.goto(-40,50)
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()


t.ht()
t.color("red")
t.home()
t.color("red")
t.goto(20,160)
t.color("cyan")
t.begin_fill()
t.circle(50)
t.end_fill()

t.ht()
t.color("red")
t.home()
t.color("red")
t.goto(-40,240)
t.color("plum")
t.begin_fill()
t.circle(50)
t.end_fill()
t.hideturtle()
win.exitonclick()




