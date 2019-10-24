# how to replace underscores with letters

mystery = "halloween"
mystery = list(mystery)

guessList = "_________"
guessList = list(guessList)

guess = input("Guess a letter: ")

if guess in mystery:
	count = 0
	for letter in mystery:
		count = count + 1
		if letter == guess:
			guessList[count] = guess


print(guessList)