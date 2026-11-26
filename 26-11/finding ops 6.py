def  f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
f1([10 , 20] , {30 , 40} , (50 , 60))
