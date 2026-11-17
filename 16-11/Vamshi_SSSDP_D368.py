a=['laptop','mouse','keyboard','monitor','printer']
b=eval(input('enter list element:'))
if(b in a):
    print('True')
else:
    print('false')


a=int(input('enter account balance:'))
b=int(input('enter withdrawl amount:'))
if(a>b):
    print('withdrawl successful!')
    print(f'remaining balance: rs.{a-b}')
else:
    print('insufficient balance')

a=float(input('enter electricity units'))
units='low consumption'if a<100 else 'medium consumption' if a<=300 else 'high consumption' if a<=500 else 'very high consumption'
print('consumption category:',units)
