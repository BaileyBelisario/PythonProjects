def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Bailey")

def rage():
    print("I HATE YOU!")

greetings = be_polite(greet)

greetings()

greetings = be_polite(rage)

greetings()
