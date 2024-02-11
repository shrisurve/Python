#Write a Python script to create a Class which Performs Basic Calculator Operations.

class Calculator:
	def __init__(self):
		pass

	def add(self, x, y):
		return x + y

	def sub(self, x, y):
		return x - y

	def multi(self, x, y):
		return x * y

	def div(self, x, y):

		if y != 0:
			return x / y

		else:
			return "Error: Division By Zero"


calculator = Calculator()

result_add = calculator.add(10, 7)
result_sub = calculator.sub(5, 3)
result_multi = calculator.multi(5, 3)
result_div = calculator.div(10, 0)

print("Addition: ",result_add)
print("Subtraction: ",result_sub)
print("Multiplication: ",result_multi)
print("Division: ",result_div)