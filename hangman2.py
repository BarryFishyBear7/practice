import random

mysteryWord = ["mississippi", "week", "kinship", "headquarters", "slippery", "frighten", "wire", "singer", "building", "election", "confuse", "joy", "lobby", "morsel", "flavor", "benefit"]
word = random.choice(mysteryWord)

myList = list(word)

correctLetters = []
guessList = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet)

misses = 0

print("Welcome to the Hangman Game!")
possibleMisses = input("How many times do you want to miss before you lose? ")

for letter in myList:
		correctLetters.append("_")
print(correctLetters)

while True:
	guess = input("Guess a letter: ")
	if len(guess) > 1 or guess not in alphabet:
		print("Please choose a valid letter")
	if guess in word:
		count = 0
		for letter in word:
			count = count + 1
			if letter == guess:
					correctLetters[count-1] = guess
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
	if correctLetters == myList:
		print("Victory! You've guessed the word! ")
		print("The word was " + word)
		break