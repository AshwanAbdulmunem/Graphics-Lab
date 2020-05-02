import turtle
t = turtle.Turtle()
def draw_sq():
    for i in range(0,4):
        t.fd(50)
        t.lt(90)

    t.fd(175)


def draw_Tri():
    for i in range(0, 3):
        t.fd(50)
        t.lt(120)

    t.fd(75)

draw_sq()
draw_Tri()
turtle.done()

