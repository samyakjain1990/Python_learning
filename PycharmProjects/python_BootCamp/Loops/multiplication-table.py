# Example: Print Multiplication table of a first 5 numbers using for loop and while loop

for num in range (1,6):
	#j = 1
	print(f"Multiplication table of {num}:")
	for j in range (1,11):
		out = num*j
		print (out,end=' ')
	print(' ')