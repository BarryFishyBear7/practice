import random

mysteryWord = ["number", "stifle","crayon", "native", "coward", "kindly", "python", "player", "melody", "method"]
word = random.choice(mysteryWord)

myList = list(word)

correctLetters = []
wrongLetters = []
guessList = []

misses = 0

print("Welcome to the Hangman Game!")
possibleMisses = input("How many times do you want to miss before you lose? ")

for letter in myList:
		correctLetters.append("_")
print(correctLetters)

while True:
	guess = input("Guess a letter: ")
	if guess in word:
		index = myList.index(str(guess))
		correctLetters.pop(int(index))
		correctLetters.insert(int(index), guess)
		print(correctLetters)
		print("Misses: " + str(guessList))
		print("You can miss " + str(int(possibleMisses) - int(misses)) + " more times")
	if guess not in word:
		misses = misses + 1
		guessList.append(guess)
		print(correctLetters)
		print("Misses: " + str(guessList))
		print("You can miss " + str(int(possibleMisses) - int(misses)) + " more times")
	if misses == int(possibleMisses):
		print("Game over!")
		print("The word was " + word)
		break
	if correctLetters[0] == myList[0] and correctLetters[1] == myList[1] and correctLetters[2] == myList[2] and correctLetters[3] == myList[3] and correctLetters[4] == myList[4] and correctLetters[5] == myList[5]:
		print("Victory! You've guessed the word! ")
		break