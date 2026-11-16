import math
x,y=eval(input('enter a tuple of(x-coordinate,y-coordinate):'))
r=float(input('enter radius of a circle:'))
dist=math.sqrt(x**2+y**2)
if(dist==0):
    print('point is on the origin')
if(dist<r):
    print('point is inside the circle')
if(dist>r):
    print('point is outside of a circle')
