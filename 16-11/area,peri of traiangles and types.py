import math
a=int(input('enter 1st side:'))
b=int(input('enter 2nd side:'))
c=int(input('enter 3rd side:'))
if a+b>c and b+c>a and c+a>b:
    if a==b==c:
        print('it is equilateral triangle')
        area=math.sqrt(3)/4*a**2
        print('area of triangle:',area)
    elif a==b or b==c or a==c:
        print('it is isosceles triangle')
        perimeter=a+b+c
        print('perimeter of triangle:',perimeter)
    else:
        print('it is scalene triangle')
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        perimeter=a+b+c
        print('area of triangle:',area)
        print('perimeter of triangle:',perimeter)
