for x in range(1,20):
	if x == 4 or x == 13:
		print(f"{x}: UNLUCKY!")
	elif x % 2 == 0:
		print(f"{x}: Even")
	else:
		print(f"{x}: Odd")

