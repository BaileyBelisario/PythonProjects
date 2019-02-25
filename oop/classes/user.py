class User:

    active_users = 0

    def __init__(self,first=None,last=None,age=None):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out'

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.first[0]}."

    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th, {self.first}'

user1 = User('Bailey','Belisario',20)
user2 = User('John','Doe',0)

print(user1.first,user1.last)

print(user2.full_name())

print(user1.initials())

print(user1.likes('ice cream'))

print(user2.likes('chips'))

print(user1.birthday())

print(user1.age)

print(User.active_users)

print(user1.logout())
