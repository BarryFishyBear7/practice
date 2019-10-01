# Brian Liu
# P1 9/27/19
# guessinggame.py

import random 

mysteryNumber = random.randint(1, 100)

score = 0

while True:
	guess = int(input("Pick a number between 1 and 100: "))
	score = score + 1

	if guess == mysteryNumber:
		print("Good guess! ")
		break
	elif guess > mysteryNumber:
		print("Too high, try again ")
	else:
		print("Too low, try again ")


print("It took you " + str(score) + " guesses")
