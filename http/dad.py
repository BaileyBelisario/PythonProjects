import requests
from os import system
from random import randint
import pyfiglet
from termcolor import colored

system("clear")

msg = 'Dad Jokes Generator'
color = 'blue'

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)

topic = input('Let me tell you a joke! Give me a topic: ')

url = 'https://icanhazdadjoke.com/search'

res = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={'term': topic}
)

data = res.json()

amount_jokes = data['total_jokes']

if amount_jokes == 0:
    print(f"Sorry! I do not have any jokes about {topic}. Please try again.")
else:
    print(f"I've got {amount_jokes} jokes about {topic}. Here it is:")

    random_joke = randint(0, amount_jokes - 1)
    result = data['results']
    joke = result[random_joke]['joke']

    print(joke)
