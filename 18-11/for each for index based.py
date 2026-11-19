a=[25,10.8,'hyd',True]
print('indexed based for loop')
for x in reversed(a):
    print(x,end='\n')
print()
for i in range(len(a)-1,-1,-1):
    print(a[i],end='\n')
print()
