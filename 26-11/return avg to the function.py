def  avg(*a):
	return sum(a)/len(a) if len(a)>0 else 0
print(avg(10 , 20 , 15 , 18))  #  (10 + 20 + 15 + 18) / 4
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
#tpl = (10 , 20 , 15 , 18)
#print(avg(tpl))


'''
15.75
12.266666666666666
14.26
0
25.0
(4+5j)
'''
