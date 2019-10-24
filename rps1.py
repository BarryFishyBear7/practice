# Brian Liu P1 
# Rock Paper Scissors Game

#__________________________________________________________________________________________________________________________________________________________________________________________________________

# break into pieces:
# welcome page, with name entry 
# score screen with computer, player (name), ties
# gives options for game r,p,s,q
# game will loop until q is entered
# each loop it will get a random choice from the computer,
# a choice from the player, compare the two, and update the score
# when the game is over (q is entered) it shows final score

# WELCOME PAGE
# prompt for the player's name
# a welcome message

#__________________________________________________________________________________________________________________________________________________________________________________________________________

# imports

import random

# variables

playerScore = 0
computerScore = 0
ties = 0

# make a list
cChoices = ["r", "p", "s"]

print("Welcome to Rock Paper Scissors")
name = input("Enter your name: ")

while True:
	# print the score
	print("The score is: ")
	print("Computer: " + str(computerScore))
	print(name + ": " + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit: ")
	computerChoice = random.choice(cChoices)
	if choice == "q": 
		break

	if choice == "r": 
		print(name + " picked Rock")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rock")
			computerScore = computerScore + 1
		else:
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore = playerScore + 1

	elif choice == "p":
		print(name + " picked Paper")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("Paper beats Rock")
			playerScore = playerScore + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		else:
			print("Computer picked Scissors")
			print("Scissors beats Paper")
			computerScore = computerScore + 1
	elif choice == "s":
		print(name + " picked Scissors")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors")
			computerScore = computerScore + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Scissors beats Paper")
			playerScore = playerScore + 1
		else:
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
	else: # if you type something besides r, p, s, or q
		print("This is an invalid choice, pick again")

print("Final score: ")
print("Computer: " + str(computerScore))
print(name + ": " + str(playerScore))
print("Ties: " + str(ties))