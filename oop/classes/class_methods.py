class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(',')
        return cls(first,last,int(age))

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
