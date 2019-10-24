# changing string to list

myString = "Arizona"
mysteryWord = list(myString)
print(mysteryWord)
guessList = []

# how to make a list with _ for characters

for letter in mysteryWord:
	guessList.append("_")

print(guessList)

# how to replace a specific index in a list

guessList[3] = "z"
print(guessList)