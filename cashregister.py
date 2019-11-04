# Brian Liu
# P1

nickels = 0
dimes = 0
quarters = 0
halfDollars = 0
dollars = 0
change = 0

price = float(input("What is the price of the item? "))
given = float(input("How much money was given? "))

change = given - price
print("Change: " + "$" + str(round(change, 2)))

change = change * 100

dollars = change / 100
change = change % 100
change = round(change)

halfDollars = change / 50
change = change % 50
change = round(change)

quarters = change / 25
change = change % 25
change = round(change)

dimes = change / 10
change = change % 10
change = round(change)

nickels = change / 5
change = change % 5
change = round(change)

print("Dollars: " + str(int(dollars)))
print("Half Dollars: " + str(int(halfDollars)))
print("Quarters: " + str(int(quarters)))
print("Dimes: " + str(int(dimes)))
print("Nickels: " + str(int(nickels)))
print("Pennies: " + str(int(change)))