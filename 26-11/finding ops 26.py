def  f1():
	#a = 20
	global   a
	#print(a)
	print(globals()['a'])
	a = 30
	globals()['a'] = 40
a = 10
print(a)
a += 1
f1()
print(a)
