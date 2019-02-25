age = input("What is your age?\n")
if age:
	age = int(age)
	if age >= 21:
		print("You can enter and drink!")
	elif age >= 18:
		print("You will recieve a wristband")
	else:
		print("Sorry you are too young to enter the event")
else:
	print("Please enter an age")
