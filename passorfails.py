#write a code for check student has passed or failed by taking marks in 3 subject

html = int(input('Enter the html subject marks: '))
java = int(input('Enter the java subject marks: '))
python = int(input('Enter the python subject marks: '))

if html>=45 and java>=45 and python>=45:
	print('Passed')
else:
	print('Failed')