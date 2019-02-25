# use isinstance(instance, class) to see if something is inheriting from
# another class


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f'this animal says {sound}')


class Cat(Animal):
    def __init__(self, name, breed, toy):
        # uncommon
        # Animal.__init__(self,name,species)
        # common
        super().__init__(name, species="Cat")

        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


blue = Cat('Blue', 'Scottish Fold', 'String')
print(blue.name)
