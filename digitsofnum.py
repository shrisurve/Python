#count number digits

num = int(input('Enter the Number '))
count=0
while num!=0:
 r=num%10
 print(r)
 count+=1
 num=num//10

print('Total Number of digits: ',count)
