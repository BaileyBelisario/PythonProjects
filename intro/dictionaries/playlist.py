#if you have a list of pairs, you can just use dict(list) to make a dictionary
#you can loop through a list to make a dictionary

playlist = {
	'title': 'patagonia bus', 
	'author': 'bailey', 
	'songs': [
		{'title': 'song', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'dj kat'], 'duration': 5.5}
	]
}

total_length = 0

for song in playlist['songs']:
	total_length += song['duration']

print(total_length)


numbers = dict(first=1, second=2, third=3)			

newnum = {key: value ** 2 for key,value in numbers.items()}

print(newnum)

squared = {x: x ** 2 for x in range(1,6)}

print(squared)

evenodd = {x:("even" if x % 2 == 0 else "odd") for x in range(1,5)}
print(evenodd)

asciilist = {i:chr(i) for i in range(65,91)}
print(asciilist)
