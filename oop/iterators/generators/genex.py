def nums():
    for num in range(1,10):
        yield num

g = nums()
#same
#g = (num for num in range(1,10))

