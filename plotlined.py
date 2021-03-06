"""
DOTLINE
"""
import matplotlib.pyplot as plt
import numpy as np
plt.axis([-20,130,80,-20])
plt.axis('on')
plt.grid(True)
plt.arrow(0,0,20,0,head_length=4,head_width=3,color='k')
plt.arrow(0,0,0,20,head_length=4,head_width=3,color='k')
plt.text(25,-3,'x')
plt.text(-5,25,'y')
#———————————————————green line
x1 = 20
x2 = 120
y1 = 80
y2 = 35
q = np.sqrt((x2-x1)**2+(y2-y1)**2)
ux = (x2 - x1) / q
uy = (y2 - y1) / q

for l in np.arange(0, q, 1):
  px = x1 + l * ux
  py = y1 + l * uy
  plt.scatter(px, py, s=1, color='r')


x1 = 30
x2 = 150
y1 = 80
y2 = 35
q = np.sqrt((x2-x1)**2+(y2-y1)**2)
ux = (x2 - x1) / q
uy = (y2 - y1) / q

for l in np.arange(0, q, 1):
  px = x1 + l * ux
  py = y1 + l * uy
  plt.scatter(px, py, s=1, color='y')

 #———————————————————————————————————————————blue line
x1 = 20
x2 = 120
y1 = 60
y2 = 25
q = np.sqrt((x2-x1)**2+(y2-y1)**2)
ux = (x2 - x1) / q
uy = (y2 - y1) / q

for l in np.arange(0, q, 1):
  px = x1 + l * ux
  py = y1 + l * uy
  plt.scatter(px, py, s=1, color='b')
plt.show()