num=int (input("Enter the Number: "))
fact=1
if num<0:
	print("Cant find negative number factors")
elif num==0:
	print("Zero number have only one factor")
else:
	for i in range(1,num + 1):
		fact = fact*i


print("Factorial of ",num,"is ",fact)

