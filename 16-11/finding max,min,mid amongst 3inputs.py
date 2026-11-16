a=int(input('enter 1st input:'))
b=int(input('enter 2nd input:'))
c=int(input('enter 3rd input:'))
max=a
if(b>a):
    max=b
if(c>a):
    max=c
min=a
if(b<a):
    min=b
if(c<a):
    min=c
mid=(a+b+c)-(max+min)
print('largest input:',max)
print('smallest input:',min)
print('middle input:',mid)
