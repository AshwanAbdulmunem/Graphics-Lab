import turtle
color('red','yellow')
  turtle.begin_fill()
      while True:
          forward(200)
          left(170)
          if abs(pos())<1:
              break
          turtle.end_fill()
          done()
      
