#.values gets the values
#.keys gets the keys
#.items grabs the key and value
#.clear will empty out a dictionary
#.copy will copy a dictionary
#{}.fromkeys will create dictionary and put value for multiple keys
#.get will get the value from a key inputted
#dict.fromkeys will grab all the keys from dictionary and then you enter value, (dictionary, value)
#.pop will remove from dictionary with provided key
#.popitem will remove randomly from dictionary
#.update will take everything from a another dictionary and update the new one


newlist = dict(name = "Bailey", owns_dog = True, num_courses = 5, fav_lang = "Python")

for x in newlist.values():
	print(x)

for x in newlist.keys():
	print(x)

for x,v in newlist.items():
	print(f"Key: {x}  Val: {v}")


full = {}.fromkeys(['name','number','height','weight'], None)

print(full)

full.pop('name')
print(full)
full.popitem()
print(full)
new = newlist.copy()
print(new)

def multiple_letter_count(string):
	return{letter: string.count(letter) for letter in string}
