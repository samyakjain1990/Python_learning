# Example: break the loop if number a number is greater than 15

numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]

for num in numbers:
	if num > 15:
		print("The number is bigger than 15")
		break
	else:
		print ("The number is smaller than 15:%s",num)