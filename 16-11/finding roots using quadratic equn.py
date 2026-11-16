import math
a=float(input('enter 1st input:'))
b=float(input('enter 2nd input:'))
c=float(input('enter 3rd input:'))
disc=(b**b)-4*a*c
if(disc>0):
    print('roots are real and distinct')
    r1=-b+math.sqrt(disc)/2*a
    r2=-b-math.sqrt(disc)/2*a
    print(f'root1:{r1}:.2f')
    print(f'root2:{r2}:.2f')
elif(disc==0):
    print('roots are real and equal')
    r1=-b/2*a
    r2=r1
    print('root1:',r1)
    print('root2:',r2)
else:
    print('roots are real and imaginary')
    real=-b/2*a
    imag=-math.sqrt(-disc)/2*a
    print('root1:',complex(real,imag))
    print('root2:',complex(real,imag))


#output:
#enter 1st input:3
#enter 1st input:3
#enter 2nd input:7
#enter 3rd input:2
#roots are real and distinct
#root1:1354.2192145279173:.2f
#root2:-1368.2192145279173:.2f




    
