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

class Moderator(User):
    total_moderators = 0

    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.total_moderators += 1

    @classmethod
    def display_active_moderators(cls):
        return f"There are currently {cls.total_moderators} active moderators."

    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.community} community"

jasmine = Moderator("Jasmine","O'Connor",61,"Piano")
print(jasmine.full_name())
print(jasmine.community)


print(User.display_active_users())
print(Moderator.display_active_moderators())


print(Moderator.mro())

print(help(Moderator))









