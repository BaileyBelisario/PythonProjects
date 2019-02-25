#use isinstance(instance, class) to see if something is inheriting from another class

class Animal:
    cool = True

    def make_sound(self, sound):
        print(f'this animal says {sound}')

class Cat(Animal):
    pass

blue = Cat()
blue.make_sound('meow')
