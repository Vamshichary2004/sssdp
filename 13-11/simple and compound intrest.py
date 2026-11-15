p=float(input('enter principle:'))
t=float(input('enter time:'))
r=float(input('enter rate of intrest:'))
si=p*t*r/100
ci=p*(1+r/100)**t-p
print("si:",si)
print("ci:",ci)


