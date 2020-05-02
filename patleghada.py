import turtle
t=turtle.Turtle()
t.speed(20)
t.getscreen().bgcolor("#905047")
def draw_petal():
    for i in range(13):
        t.fillcolor("#d84d7a")
        t.begin_fill()
        t.left(360 / 10)
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.end_fill()

draw_petal()
turtle.done()
