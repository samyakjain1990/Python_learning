#Example: Calculate the average of list of numbers
#==================================================

numbers = [10, 20, 30, 40, 50]

sum1  = 0
for num in numbers:
	sum1  += num

#calcluate the avg or divide by 2 
avg =  sum1/2
print("the avg or divide by 2 of number:",avg)

#calculate the avg of the number
lenth = len(numbers)
avg1 = sum1/lenth
print("the avg of number:",avg1)