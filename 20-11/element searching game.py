a=eval(input('enter any list:'))
while True:
    b=eval(input('enter the element to be searched:'))
    if(b in a):
        print('found at index:',a.index(b))
    else:
        print('not found')
    ch=input('would u like to search for another element (y/n):')
    if(ch.lower()!='y'):
        break
