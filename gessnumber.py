import random

n = random.randint(1,10)
gess = 0

while gess != n:
	guess = int(input('Gess a number '))

	if guess < n:
		print('It is Smaller')

	elif guess > n:
		print('Is is Larger')

	else:
		print('Correct Guess')