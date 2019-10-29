#import the random package so that we can generate a random choice
from random import randint

# choices is an array => an array is a container that can hold multiple values
choices = ["rock" , "paper" , "scissors"]

# set the computer variable to one of these choice (0, 1 or 2)
computer = choices [randint(0, 2)]

#set up the game loop so that we don't have to restart all the time 

player = False 

while player is False:
	# set player to True
	print("************************\n\n")
	print("choose your weapon!\n\n")
	print("************************\n\n")

	player = input("choose rock, paper, paper or scissors\n")

	print("computer chose", computer, "\n")
	print("player chose", player, "\n")

	if player.lower()== "quit":
		 exit()

	elif computer == player:
		print("tie! no one wins, play again")
	elif player == "rock":
		if computer == "paper":
			print("you lose!", computer, "covers" , player, "\n")
		else:
			print("you win!", player, "smashes through", computer, "\n")


	elif player.lower() == "paper":
		if computer == "scissors":
			print("you lose!", computer, "cuts" , player, "\n")
		else:
			print("you win!", player, "covers", computer, "\n")


	elif player.lower() == "scissors":
		if computer == "rock":
			print("you lose!", computer, "smashes" , player, "\n")
		else:
			print("you win!", player, "cuts", computer, "\n")


	else:
		print("That's not a valid choice, try again")



	#need to check all of our conditions after checking for a tie
	player = False
	computer = choices[randint(0, 2)]