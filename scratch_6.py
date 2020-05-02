import turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.color("red")
t.speed(0)
numberOfSides = 9
lengthOfSide = 100
exteriorAngle = 360 / numberOfSides
for i in range(200):
    t.forward(lengthOfSide)
    t.right(exteriorAngle)
    lengthOfSide = lengthOfSide - 0.5
turtle.done()