def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError as err:
        print("Do not divide by zero please")
        print(err)
    except TypeError as err:
        print("A and B must be ints and floats")
        print(err)
    else:
        print(f"{a}/{b} is equal to {result}")



divide('a',3)
divide(1,2)
divide(1,0)
