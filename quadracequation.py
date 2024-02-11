import math
a = int(input('enter the A value '))
b = int(input('enter the B value '))
c = int(input('enter the C value '))
root1 =(-b + math.sqrt(b**2-4*a*c))/(2*a)
root2 =(-b - math.sqrt(b**2-4*a*c))/(2*a)

print('Roots are: ',root1,root2)