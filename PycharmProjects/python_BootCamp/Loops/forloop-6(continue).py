# Example: Count the total number of ‘m’ in a given string.

name = "mariya mennen"

count = 0
for char in name:
	if char != 'm':
		continue	#with continue the whole line of statements after continue will skip 
	else:
		count +=1
print("The count is ",count)