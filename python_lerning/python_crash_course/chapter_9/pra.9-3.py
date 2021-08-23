#pra.9-3 inP144
class User:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is now {self.age}.")

    def greet_user(self):
        print(f"Hello,{self.first_name} {self.last_name}.")


user1 = User('Ada','lovelace',49)
user2 = User('Eric','Mases',51)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
