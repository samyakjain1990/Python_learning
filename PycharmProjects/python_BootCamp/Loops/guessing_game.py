import random
x =0
random_no = random.randint(1,10) 
# guess the number between 1-10

while True:
	x = int(input ("Enter the number between 1 and 10:"))
	
	if x > random_no:
		print("You guess is higher than the correct number")
		print (x)
		print (random_no)
	elif x < random_no:
		print("You guess is lower than the correct number")
		print (x)
		print (random_no)
	else:
		print("You guess the correct number")
		user_selection=input ("Do you want to play again ? (y/n) : ")
		if user_selection == "y":
			random_no = random.randint(1,10) 
			x = None
		else:
			print("Thank you for playing")
			break