num_of_nos = int(input('Enter the number to take input: '))
psum=0
nsum=0
count=0
while count<num_of_nos:
	num = int(input('Enter the Number: '))
	count += 1
	if num > 0:
		psum += num
	else:
		nsum += num

print('Positive Number Sum is: ',psum)
print('Negative Number Sum is: ',nsum)