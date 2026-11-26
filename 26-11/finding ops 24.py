def  f1():
        global  a
        print(a)
        a += 1
def  f2():
        global  a
        print(a)
        a += 1
a = 10
print(a)
a += 1
f1()
print(a)
a += 1
f2()
print(a)
