print("rock")
print("paper")
print("scissors")

player1 = input("player1 : Please enter the option which you want to select:")
player2 = input("player2 : Please enter the option which you want to select:")

if ((player1 != "rock")or (player1 != "paper")or (player1 != "scissors")):
    if ((player2 != "rock")or (player2 != "paper")or (player2 != "scissors") ):
        if (player1 == 'rock') and (player2 == 'paper'):
            print("player 2 wins")
        elif(player1 == 'rock') and (player2 == 'scissors'):
            print("player 1 wins")
        elif(player1 == 'paper') and (player2 == 'rock'):
            print("player 1 wins")
        elif(player1 == 'paper') and (player2 == 'scissors'):
            print("player 2 wins")
        elif(player1 == 'scissors') and (player2 == 'rock'):
            print("player 2 wins")
        elif(player1 == 'scissors') and (player2 == 'paper'):
            print("player 1 wins")
        elif(player1 == player2):
            print("It is a tie")
else:
    print("Incorrect input")