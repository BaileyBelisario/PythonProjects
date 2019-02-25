#sets cannot have duplicates
#.add value to set
#.remove value from set
#.discard if you want no errors when removing non existent
#.copy will copy a set newset = set.copy()
#.clear will clear
#declare sets with {}

# | is union will join 2 sets and get rid of duplicates
# & will get the unique ones that are in both sets


s = set({1,2,3,4,5,6})

print(s)

newlist = [1,2334,5,5,67,7,67,6,5,4,33,54,5,6,67]

print(len(set(newlist)))

print(list(set(newlist)))

newset = {x**2 for x in range(0,10)}
print(newset)

charset = {char.upper() for char in 'hello'}
print(charset)
