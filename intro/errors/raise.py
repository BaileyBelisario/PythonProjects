def colorize(text, color):
    colors = ('cyan','yellow','blue','green','magenta')
    if type(text) is not str:
            raise TypeError("Text must be an instance of str")
    if color not in colors:
            raise ValueError("Color is an invalid color")

    print(f"Printed {text} in {color}")

colorize("hello","red")
