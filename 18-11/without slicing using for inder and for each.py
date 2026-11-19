from itertools import islice
a=[25,10.8,'hyd',True,3+4j,None,'SEC']
print('indexed for loop')
for i in range(2,5):
    print(a[i])
print()
print('using for each')
for x in islice(a,2,5):
    print(x)
print()
