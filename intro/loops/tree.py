height = int(input("\nHow tall do you want the tree?\n"))

if height % 2 == 0:
	height += 1

for x in range(height):
	if x % 2 == 1:
		spaces = int(height-(x/2)) 
		print(" " * spaces + "*" * x)

for x in range(3):
	print(" " * int(height-2) + "***")
