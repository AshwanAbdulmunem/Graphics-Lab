from turtle import *
space = Screen()
tess = Turtle()
tess.color("blue")
tess.shape("turtle")

print(range(5, 60, 2))
tess.penup()                  # ask tess to pick up her pen
for size in range(5, 60, 2):
          # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)
          print(size)
          # move tess along
    tess.right(24)
   turtle.done()
