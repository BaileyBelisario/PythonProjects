#.count will count how many of the same value there are
#.index will return the index of a given value



months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')


locations = {
	(35.6895, 39.6917): 'Tokyo Office',
	(42.5675, 74.5678): 'New York Office',
	(37.4555, 122.345): 'San Fran Office'
	
}

cat = {'name':'biscuit','age':0.5}
tuplecat = cat.items()
print(cat)
print(tuplecat)

for x,k in cat.items():
	print(f"Key: {x} --- Value: {k}")

for x in months:
	print(x)
