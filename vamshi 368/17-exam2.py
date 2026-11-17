a=int(input('enter account balance:'))
b=int(input('enter withdrawl amount:'))
if(a>b):
    print('withdrawl successful!')
    print(f'remaining balance: rs.{a-b}')
else:
    print('insufficient balance')
          
      
