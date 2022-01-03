import random

print("Rock..")
print("Paper..")
print("Scissors..")

# taking the input from the user
_player1_ = input("Enter the value for player1: ")
_randomnumber_ = random.randint(0,2)
if _randomnumber_ == 0:
	_computer_ = "rock"
elif _randomnumber_ == 1:
	_computer_ = "paper"
else:
	_computer_ = "scissors"	

# values of Player1 and computer 
print("The value entered by player1: "+ _player1_)
print("The value entered by computer: "+_computer_)

if _player1_ == _computer_:
	print ("Game is draw")
elif _player1_ == "rock":
	if _computer_ == "scissors":
		print("Player1 wins")
	elif _computer_ == "paper":
		print("Player2 wins")
	else:
		print ("Something went wrong or wrong input")
elif _player1_ == "paper":
	if _computer_ == "rock":
		print("Player1 wins")
	elif _computer_ == "scissors":
		print("Player2 wins")
	else:
		print ("Something went wrong or wrong input")
elif _player1_ == "scissors":
	if _computer_ == "rock":
		print("Player2 wins")
	elif _computer_ == "paper":
		print("Player1 wins")
	else:
		print ("Something went wrong or wrong input")
else:
 	print("Something went wrong or wrong input")