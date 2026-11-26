def  concat(*a):
	return ' '.join(a) if len(a)>0 else 0
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
#print(concat(1, 2, 3))

'''
Sankar Dayal Sarma
Hyd Is Green City
Python Is A Great Language
0
Python
'''
