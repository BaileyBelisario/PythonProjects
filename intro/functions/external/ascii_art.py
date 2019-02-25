import pyfiglet
from termcolor import colored

msg = input("What would you like to print?")
color = input("What color? ")

colorlist = ("red","yellow","green","blue","magenta","cyan")

if color not in valid_colors:
    color = "magenta" 

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)

