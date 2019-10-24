# Checking if word=word

myWord = "hello"

choice = input("Type a word: ")

if choice == myWord:
	print("It's a match")
else:
	print("Not a match")


# Checking if a letter is in a word

letter = input("Type a letter: ")

if letter in myWord:
	print("Letter is in the word")
else:
	print("Letter isn't in the word") 

count = 0
for letter2 in myWord:
	count = count + 1
	if letter2 == letter:
		print(count)