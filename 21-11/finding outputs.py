def  f1():
	return   10 , 20 , 30
# End  of  the  function
x = f1()
print(x)
print(type(x))
a , b , c =  f1()   
print(a)
print(b)
print(c)
print('for  loop')
for  x   in   f1():
	print(x)
	
	
'''
(10, 20, 30)
<class 'tuple'>
10
20
30
for  loop
10
20
30
'''