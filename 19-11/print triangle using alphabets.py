n=int(input('enter number of lines:'))
for i in range(1,n+1):
    print(" "*(n-1),end='')
    for j in range(1,i+1):
        print(chr(64+j),end='')
    print()
