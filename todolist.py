# Brian Liu
# P1 10/17/19

print("Welcome to To Do List")
todolist = []
while True:
	print("enter 'a' to add an item")
	print("enter 'r' to remove an item")
	print("enter 'p' to print the list")
	print("enter 'q' to quit")
	choice = input("Choose: ")
	if choice == "q":
		break
	elif choice == "a":
		add = input("What do you want to add to your to do list? ")
		todolist.append(add)
	elif choice == "r":
		remove = input("What do you want to remove from your to do list? ")
		todolist.remove(remove)
	elif choice == "p":
		print(todolist)
	else: 
		print("Please choose a valid option. ")