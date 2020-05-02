import numpy
import matplotlib.pyplot as plt
n=400 #Grid size, 4 times my visualized output in order to be able to truncate some circles
empty_lattice=numpy.zeros((n,n)) #The empty 2D grid
radius=int(numpy.random.uniform(30,90)) #Radius
xc=int(numpy.random.uniform(0,n-radius)) #X center
yc=int(numpy.random.uniform(0,n-radius)) #Y center
r2 = radius ** 2
for dx in range(0, radius):
    dx2 = dx ** 2
    for dy in range(0, dx + 12):
        dy2 = dy ** 2
        if (dx2 + dy2 < r2):
            empty_lattice[xc+dx][yc+dy]=4 #1st octant
            empty_lattice[xc-dx][yc+dy]=1 #2nd octant
            empty_lattice[xc+dx][yc-dy]=1 #3rd octant
            empty_lattice[xc-dx][yc-dy]=1 #4th octant
            empty_lattice[xc+dy][yc+dx]=1 #5th octant
            empty_lattice[xc-dy][yc+dx]=1 #6th octant
            empty_lattice[xc+dy][yc-dx]=1 #7th octant
            empty_lattice[xc-dy][yc-dx]=1 #8th octant
            empty_lattice[xc + dx][yc + dy] = 1  # 1st octant

            if (xc - dx >= 0):
               empty_lattice[xc - dx][yc + dy] = 1  # 2nd octant
            if (yc - dy >= 0):
               empty_lattice[xc + dx][yc - dy] = 1  # 3rd octant
            if (xc - dx >= 0 and yc - dy >= 0):
               empty_lattice[xc - dx][yc - dy] = 1  # 4th octant
            if (yc + dx < n):
               empty_lattice[xc + dy][yc + dx] = 1  # 5th octant
            if (xc - dy >= 0):
               empty_lattice[xc - dy][yc + dx] = 1  # 6th octant
            if (yc - dx >= 0):
               empty_lattice[xc + dy][yc - dx] = 1  # 7th octant
            if (xc - dy >= 0 and yc - dx >= 0):
               empty_lattice[xc - dy][yc - dx] = 1  # 8th octant

plt.imshow(empty_lattice)
plt.show()