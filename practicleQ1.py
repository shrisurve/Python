#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def count_upper_lower(string):
	upper_count= 0
	lower_count= 0

	for char in string:
		if char.isupper():
			upper_count += 1


		elif char.islower():
			lower_count += 1

	return upper_count, lower_count
	
input_string = "ShrikanT SurvE"
upper, lower = count_upper_lower(input_string)

print("Upper case letter: ",upper)
print("Lower case letter: ",lower)

