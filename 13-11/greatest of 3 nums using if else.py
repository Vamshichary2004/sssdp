x=int(input('enter 1st element:'))
y=int(input('enter 2nd element:'))
z=int(input('enter 3rd element:'))
if(x>y and x>z):
    print(f'{x} is greatest')
elif(y>z):
    print(f'{y} is greatest')
else:
    print(f'{z} is greatest')
    
