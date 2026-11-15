x=int(input('enter 4 digit year:'))
if(x%4==0)or(x%4==0 and x%100!=0):
    print(f'{x} is a leap year')
else:
    print(f'{x} is not a leap year')
    
