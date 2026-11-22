a=eval(input('enter any list:'))
while True:
    b=eval(input('enter the element to be searched:'))
    c=0
    for i in range(len(a)):
        if(b==a[i]):  
            print('found at index:',i)
        if(c>0):
            print(f'found {c} times')
        else:
            print('not found')
        c+=1
    ch=input('would u like to search for another element (y/n)?:')
    if(ch.lower()!='y'):
        break
