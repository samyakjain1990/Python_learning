# for 4 and 13, print x is unlocky"
# for even numbers , print "x is even"
# for odd numbers , print "x is odd"

# EXAMPLE:1
# ============
# num = input ("Enter the value of x: ") # taking the input for the number to be evaluated
# x = int(num)
# if (x == 4 or x ==13):
# 	print ("The nuber is unlucky")
# elif(x % 2 !=0):
# 	print("The number is even")
# else:
# 	print("The number is odd")


# EXAMPLE:2
# ============
#Lopping through range 1-x and print numbers

num = input ("Enter the value for range to evaluated: ") # taking the input for the number to be evaluated
x = int(num)

for x in range (1,x):
	if (x == 4 or x ==13):
		print (f"The nuber {x} is unlucky")
	elif(x % 2 !=0):
		print(f"The number {x} is even")
	else:
		print(f"The number {x} is odd")


# EXAMPLE:3
# ============
#Lopping through range 1-x and print numbers


# numf = input ("Enter the min range to evaluated: ") # taking the input for the number to be evaluated
# x = int(numf)
# numl = input ("Enter the min range to evaluated: ") # taking the input for the number to be evaluated
# y = int(numl)

# for z in range (x,y):
# 	if z == 4 or z ==13 :
# 		state = "unlucky"
# 	elif z % 2 !=0 :
# 		state = "EVEN"
# 	else :
# 		state = "ODD"
# 	print (f"The nuber {z} is {state}")