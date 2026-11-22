sum =  ctr = 0
while  True:
	try:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))  
		(sum:=sum+x,ctr:=ctr+1) 
	except  EOFError:
		try:
			print('Average : ' , sum / ctr)  
			exit()
		except  ZeroDivisionError:
			print('Enter  at  least  one  input')
	except  NameError , TypeError:
		print('Input  cannot  be  string')
		
		
'''
Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  56
Enter input  (ctrl + z  to  stop)  :  90
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :  57.0
Press any key to continue . . .
'''
