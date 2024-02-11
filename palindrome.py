num = int(input('Enter the Number to check palindrome: '))
temp=num
rev=0
while num!=0:
	rev=rev*10+num%10
	num//=10

if rev == temp:
	print('Number is Palindrome')
else:
	print('Number is not Palindrome')