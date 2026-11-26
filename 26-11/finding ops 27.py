def   f1():
	#x = x + 5
         pass
def  f2():
	x = globals()['x'] + 5
	print(x)
x = 10
f1()
f2()
print(x)
