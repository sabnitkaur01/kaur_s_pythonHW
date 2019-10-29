#import the random package so that we can generate a random choice
from random import randint

# choices is an array => an array is a container that can hold multiple values
choices = ["rock" , "paper" , "scissors"]
player_lives = 5 
computer_lives = 5
# set the computer variable to one of these choice (0, 1 or 2)
computer = choices [randint(0, 2)]

#set up the game loop so that we don't have to restart all the time 

player = False 

while player is False:
    # set player to True
    print("***************************\n\n")
    print("computer lives: ", computer_lives, "/5\n")
    print("player lives: ", player_lives, "/5\n")
    print("choose your weapon!\n\n")
    print("***************************\n\n")

    player = input("choose rock, paper, paper or scissors\n")

    print("computer chose", computer, "\n")
    print("player chose", player, "\n")

    if player.lower() == "quit":
        exit()
    elif computer == player:
        print("tie! no one wins, play again")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player, "\n")
            player_lives = player_lives - 1
        else:
            print("You win!", player, "smashes through", computer, "\n")
            computer_lives = computer_lives - 1

    elif player.lower() == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player, "\n")
            player_lives = player_lives - 1
        else:
            print("You win!", player, "covers", computer, "\n")
            computer_lives = computer_lives - 1
        
    elif player.lower() == "scissors":
        if computer == "rock":
            print("You lose!", computer, "smashes", player, "\n")
            player_lives = player_lives - 1
        else:
            print("You win!", player, "cuts", computer, "\n")
            computer_lives = computer_lives - 1

    else:
        print("That's not a valid choice, try again") 

    # handle all lives lost for player or AI
    if player_lives is 0:
       print("out of lives! you suck at this game. would you like to play again")
       choice = input("Y / N") 
       print(choice) 

       if (choice is "N") or (choice is "n"):
           print("you chose to quit.")
           exit()
       elif (choice is "Y") or (choice is "y"):
            # reset the game so that we can start all over again 
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0,2)]

    elif computer_lives is 0:
        print("out of lives! you suck at this game. would you like to play again")
        choice = input("Y / N") 
        print(choice) 

        if (choice is "N") or (choice is "n"):
           print("you chose to quit.")
           exit()
        elif (choice is "Y") or (choice is "y"):
            # reset the game so that we can start all over again 
            player_lives = 5
            computer_lives = 5
            player = False
            computer = choices[randint(0,2)]


    else:
        #need to check all of our conditions after checking for a tie
        player = False
        computer = choices[randint(0, 2)]

