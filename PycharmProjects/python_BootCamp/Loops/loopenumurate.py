#Example 1: Print elements of the list with its index number using the enumerate() function

#SOLUTION:1
#==========

numbers = [4, 2, 5, 7, 8]

# for itera,num in enumerate(numbers):
# 	print('index[',itera,']',[num])


# SOLUTION:2
#============
size = len(numbers)
for num in range(size):
	print ('index=',num ," ",'value=',numbers[num])


