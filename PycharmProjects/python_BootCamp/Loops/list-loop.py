# Example: Print the even numbers by adding 1 to the odd numbers in the list

odd = [1, 5, 7, 9]

# for num in odd:
# 	if (num%2 !=0):
# 		new_num = num +1
# 		print(new_num)


even = [num + 1 for num in odd if num%2!=0]
print(even)