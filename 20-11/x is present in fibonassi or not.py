n=10
a=0
b=1
i=1
l=[]
while(i<=n):
    l.append(a)
    a,b=b,b+a
    i=i+1
x=int(input('enter value to be searched:'))
if(x in l):
    print('found')
else:
    print('not found')
