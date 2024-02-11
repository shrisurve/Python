#write a program to check the person is eligible to work or not

age = int(input('Enter the age: '))

if age>=18 and age<=60:
	print('Eligible to work')
else:
	print('Not Eligible to work')