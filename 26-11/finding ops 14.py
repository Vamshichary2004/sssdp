def   f1():
	a = 20
	print(a)
	dict = globals()
	print(dict['a'])
	a = 30
	dict['a'] = 40
a = 10
print(a)
a += 1
f1()
print(a)

'''
10
20
11
40
'''
