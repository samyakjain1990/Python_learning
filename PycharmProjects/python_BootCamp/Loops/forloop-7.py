#  Example: Nested for loop to print the following pattern

# *
# * *
# * * *
# * * * *
# * * * * *

for i in range (1,6):
	for j in range (1,i+1):
		print ("*",end=" ")
	print('') 				# new line