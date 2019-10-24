secretWord = "christmas"
secretWord = list(secretWord)
print(secretWord)
misses = 0
hangman = ["first pic", "second pic"]

guess = input("Guess a letter: ")

if guess in secretWord:
	print("letter in word")
elif guess not in secretWord:
	misses = misses + 1

print("Misses: " + str(misses))
print(hangman[misses])
# using the number of misses as the index of the list