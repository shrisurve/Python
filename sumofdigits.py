num = int(input('Enter the Number: '))
sum=0
while num>0:
	r=num%10
	sum+=r
	num//=10

print('Sum is: ',sum)