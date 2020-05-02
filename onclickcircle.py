import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")
t.color("orange")

def circle(x, y):
    t.circle(60)


t.onclick(circle)

turtle.done()