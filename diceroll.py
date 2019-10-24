# Brian Liu P1
# Dice Roll Game

import random

rollNumber = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

print("Welcome to the Dice Roll Game!")
playerChoice = int(input("How many times do you want to roll the die? "))

while True:
	rollNumber = rollNumber + 1 
	randomNum = random.randint(1,6)
	if playerChoice == 0:
		print("Please choose a valid number")
		break
	print("Roll number: " + str(rollNumber) + " Result: " + str(randomNum))
	if rollNumber >= playerChoice:
		if randomNum == 1:
			ones = ones + 1
		elif randomNum == 2:
			twos = twos + 1
		elif randomNum == 3:
			threes = threes + 1
		elif randomNum == 4:
			fours = fours + 1
		elif randomNum == 5:
			fives = fives + 1
		elif randomNum == 6:
			sixes = sixes + 1
		break
	elif randomNum == 1:
		ones = ones + 1
	elif randomNum == 2:
		twos = twos + 1
	elif randomNum == 3:
		threes = threes + 1
	elif randomNum == 4:
		fours = fours + 1
	elif randomNum == 5:
		fives = fives + 1
	elif randomNum == 6:
		sixes = sixes + 1

print("You've rolled " + str(rollNumber) + " times. Here are your results: ")
print("Ones: " + str(ones))
print("Twos: " + str(twos))
print("Threes: " + str(threes))
print("Fours: " + str(fours))
print("Fives: " + str(fives))
print("Sixes: " + str(sixes))

print("Percentages: ")
print("Ones: " + str(((ones) / (rollNumber)*100)) + "%")
print("Twos: " + str(((twos) / (rollNumber)*100)) + "%")
print("Threes: " + str(((threes) / (rollNumber)*100)) + "%")
print("Fours: " + str(((fours) / (rollNumber)*100)) + "%")
print("Fives: " + str(((fives) / (rollNumber)*100)) + "%")
print("Sixes: " + str(((sixes) / (rollNumber)*100)) + "%")