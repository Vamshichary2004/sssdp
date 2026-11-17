a=float(input('enter electricity units'))
units='low consumption'if a<100 else 'medium consumption' if a<=300 else 'high consumption' if a<=500 else 'very high consumption'
print('consumption category:',units)
