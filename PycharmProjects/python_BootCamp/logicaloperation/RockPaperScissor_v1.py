print("Rock..")
print("Paper..")
print("Scissors..")

# taking the input from the user
_player1_ = input("Enter the value for player1: ")
_player2_ = input("Enter the value for player2: ")

if _player1_ == "rock" and _player2_ == "scissors":
	print("Player1 wins")
elif _player1_ == "rock" and _player2_ == "paper":
	print("Player2 wins")
elif _player1_ == "paper" and _player2_ == "rock":
	print("player1 wins")
elif _player1_ == "paper" and _player2_ == "scissors":
	print("player2 wins")
elif _player1_ == "scissors" and _player2_ == "rock":
	print("player2 wins")
elif _player1_ == "scissors" and _player2_ == "paper":
	print("player1 wins")
elif _player1_ == _player2_ :
	print ("Game is draw")
else:
	print("Something went wrong")
