from random import randint as r

choice = True

while choice:
	number = r(1,10)
	x = int(input("\n\nGuess a number: "))
	while x != number:
		if x > number:
			print("Too high!\n")
		else:
			print("Too Low!\n")
		x = int(input("\nGuess a number: "))
	
	print(f"\nYou got it! The number was {number}\n")
	choice = input("Would you like to play again? (y/n) ")
	if choice == 'y' or choice == 'Y':
		choice = True
	else:
		choice = False
	
print("Thanks for Playing!")
