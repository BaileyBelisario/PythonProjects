import random

d = "Draw!"
c = "Computer Wins!"
p = "Player Wins!"

choice = True
while choice:
	print("\n\n====Welcome to Rock, Paper, Scissors====\n\n")
	print("How to Play:\nChoose 'r' for 'rock'\nChoose 'p' for 'paper'\nChoose 's' for 'scissors'\n\n")

	user1 = input("Choose rock, paper, or scissors\n")
	user2 = None

	num = random.randint(1,3)
	if num == 1:
		user2 = 'r'
	elif num == 2:
		user2 = 'p'
	else:
		user2 = 's'

	if user1:
		if (user1 == 'r' or user1 == 'R') and user2 == 'r':
			print(d)
		elif (user1 == 'r' or user1 == 'R') and user2 == 's':
			print(p)
		elif (user1 == 'r' or user1 == 'R') and user2 == 'p':
        		print(c)
		elif (user1 == 'p' or user1 == 'P') and user2 == 'r':
			print(p)
		elif (user1 == 'p' or user1 == 'P') and user2 == 'p':
			print(d)
		elif (user1 == 'p' or user1 == 'P') and user2 == 's':
			print(c)
		elif (user1 == 's' or user1 == 'S') and user2 == 'r':
			print(c)
		elif (user1 == 's' or user1 == 'S') and user2 == 'p':
			print(p)
		elif (user1 == 's' or user1 == 'S') and user2 == 's':
			print(d)
	else:
		print("Player 1 did not pick a choice")

	choice = input("\nWould you like to play again?\n'y' for yes, 'n' for no\n\n")
	if choice == 'y':
		choice = True
	else:
		choice = False
