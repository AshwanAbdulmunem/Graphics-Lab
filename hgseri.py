import turtle as t

def trangle(x,a):
    p=180
    a.lt(p/3)
    a.fd(x)
    a.rt(p*2 / 3)
    a.fd(x)
    a.rt(p * 2 / 3)
    a.fd(x)
    #a.backward(x)

def t1(x,a):
    p=180
    for i in range(4):
        trangle(x/4,a)
        a.rt(180)
        a.fd(x/4)
    a.lt(180)
    a.fd(x)
    a.lt(180)

    a.lt(p / 3)
    a.fd(x/4)
    a.rt(p / 3)
    trangle(x / 4, a)
    a.lt(60)
    a.fd(x/4)
    a.lt(p * 2 / 3)
    a.lt(p / 3)
    a.fd(x/2)
    a.rt(p / 3)
    for i in range(2):
        trangle(x/4,a)
        a.rt(180)
        a.fd(x/4)
    a.rt(p*2 / 3)
    a.fd(x/4)
    a.lt(p*2 / 3)
    trangle(x / 4, a)
    a.penup()
    a.lt(60)
    a.fd(x/4)
    a.rt(60)
    a.fd(x/2)
    a.rt(180)
    a.pendown()
    a.lt(60)
    a.fd((x / 4) * 3)
    a.rt(60)
    trangle(x / 4, a)
    a.lt(60)
    a.fd((x / 4) * 3)
    a.lt(120)
    a.rt(180)


def t3(x,a):
    p = 180
    for i in range(4):
        t1(x / 4, a)
        a.rt(180)
        a.fd(x / 4)
    a.lt(180)
    a.fd(x)
    a.lt(180)

    a.lt(p / 3)
    a.fd(x / 4)
    a.rt(p / 3)
    t1(x / 4, a)
    a.lt(60)
    a.fd(x / 4)
    a.lt(p * 2 / 3)
    a.lt(p / 3)
    a.fd(x / 2)
    a.rt(p / 3)
    for i in range(2):
        t1(x / 4, a)
        a.rt(180)
        a.fd(x / 4)
    a.rt(p * 2 / 3)
    a.fd(x / 4)
    a.lt(p * 2 / 3)
    t1(x / 4, a)
    a.penup()
    a.lt(60)
    a.fd(x / 4)
    a.rt(60)
    a.fd(x / 2)
    a.rt(180)
    a.pendown()
    a.lt(60)
    a.fd((x / 4) * 3)
    a.rt(60)
    t1(x / 4, a)
    a.lt(60)
    a.fd((x / 4) * 3)
    a.lt(120)
    a.rt(180)

def t4(x):
    p = 180
    a = t.Turtle()
    a.speed(500)
    for i in range(4):
        t3(x / 4, a)
        a.rt(180)
        a.fd(x / 4)
    a.lt(180)
    a.fd(x)
    a.lt(180)
    a.lt(p / 3)
    a.fd(x / 4)
    a.rt(p / 3)
    t3(x / 4, a)
    a.lt(60)
    a.fd(x / 4)
    a.lt(p * 2 / 3)
    a.lt(p / 3)
    a.fd(x / 2)
    a.rt(p / 3)
    for i in range(2):
        t3(x / 4, a)
        a.rt(180)
        a.fd(x / 4)
    a.rt(p * 2 / 3)
    a.fd(x / 4)
    a.lt(p * 2 / 3)
    t3(x / 4, a)
    a.penup()
    a.lt(60)
    a.fd(x / 4)
    a.rt(60)
    a.fd(x / 2)
    a.rt(180)
    a.pendown()
    a.lt(60)
    a.fd((x / 4) * 3)
    a.rt(60)
    t3(x / 4, a)
    a.lt(60)
    a.fd((x / 4) * 3)
    a.lt(120)

#t4(400)

a = t.Turtle()
a.speed(500)
t3(300,a)

t.done()
