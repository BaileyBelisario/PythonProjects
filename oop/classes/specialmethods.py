from copy import copy
class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self,other):
        if isinstance(other,Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You cannot add that!"

    def __mul__(self,other):
        if isinstance(other,int):
            return [copy(self) for i in range(other)]
        return "You cannot multiply that!"

j = Human('Jenny','Larson',47)
k = Human('Kevin','Jones',49)
print(j)
print(len(j))

print(k+j)

triplets = j* 3
triplets[1].first='Jasmine'
print(triplets)

newtriplets = (k+j)*3

print(newtriplets)
