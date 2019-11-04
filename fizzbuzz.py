# Brian Liu
# P1

number = 1

while True:
	if number % 3 == 0 and number % 5 == 0:
		print(str(number), end = "")
		print(" Fizz Buzz")
	elif number % 3 == 0:
		print(str(number), end = "")
		print(" Fizz")
	elif number % 5 == 0:
		print(str(number), end = "")
		print(" Buzz")
	else:
		print(number)
	number = number + 1
	if number > 100:
		break