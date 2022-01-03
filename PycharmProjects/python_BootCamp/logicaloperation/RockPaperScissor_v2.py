print("Rock..")
print("Paper..")
print("Scissors..")

# taking the input from the user
_player1_ = input("Enter the value for player1: ")
_player2_ = input("Enter the value for player2: ")


if _player1_ == _player2_:
	print ("Game is draw")
elif _player1_ == "rock":
	if _player2_ == "scissors":
		print("Player1 wins")
	elif _player2_ == "paper":
		print("Player2 wins")
	else:
		print ("Something went wrong or wrong input")
elif _player1_ == "paper":
	if _player2_ == "rock":
		print("Player1 wins")
	elif _player2_ == "scissors":
		print("Player2 wins")
	else:
		print ("Something went wrong or wrong input")
elif _player1_ == "scissors":
	if _player2_ == "rock":
		print("Player2 wins")
	elif _player2_ == "paper":
		print("Player1 wins")
	else:
		print ("Something went wrong or wrong input")
else:
 	print("Something went wrong or wrong input")
