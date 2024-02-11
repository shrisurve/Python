num_of_nos = int(input('Enter the Number: '))
count = 0
maxno =int(input('Enter a number: '))
while count <num_of_nos-1:

	n = int(input('Enter the Number: '))
	count = count + 1
	if n > maxno:
		maxno=n
		

print('Max Number is: ',maxno)