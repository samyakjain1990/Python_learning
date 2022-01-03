# generate random number using randint(1,10) and store it in number
# generate the random number until your number does not become equal to 5
# increment the number by 1 until you get your answer

from random import randint

number = 0
i = 0

while number != 5:
	number = randint(1,10)
	i+=1
	if number ==5:
		print(f"found the number is:{number}")
		print (f"how many iterations:{i}")
	else:
		print (f"keep running the number is:{number}")
