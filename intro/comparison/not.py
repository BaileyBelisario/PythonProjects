age = int(input("What is your age?\n"))

if not ((age >= 2 and age <= 8) or age >= 65):
	print("You pay 10 Dollars and are not a child or senior")
else:
	print("You are a child or senior")

