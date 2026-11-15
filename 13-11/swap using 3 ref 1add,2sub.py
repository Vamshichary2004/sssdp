x=eval(input('enter 1st input:'))
y=eval(input('enter 2nd input:'))
print(f'before swap: {x}')
x=x+y
y=x-y
x=x-y
print(f'after swap: {x}')
