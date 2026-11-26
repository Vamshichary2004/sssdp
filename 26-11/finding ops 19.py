def  f1():
	global  a
	a = 20
	print(a)
	print(globals()['a'])
	a = 30
a = 10
print(a)
f1()
print(a)
