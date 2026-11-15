x, y = eval(input("Enter a tuple of (x co-ordinate, y co-ordinate): "))
if (x == 0 and y == 0):
    print("origin")
elif (x == 0 and y > 0):
    print("y-axis")
elif (x > 0 and y == 0):
    print("x-axis")
elif (x > 0 and y > 0):
    print("1st quadrant")
elif (x < 0 and y > 0):
    print("2nd quadrant")
elif (x < 0 and y < 0):
    print("3rd quadrant")
else:
    print("4th quadrant")
