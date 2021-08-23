#pra.9-5
class User:

    def __init__(self,first_name,last_name,age,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is now {self.age}.")

    def greet_user(self):
        print(f"Hello,{self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Ada','Lovelace',49,3)
print(user1.login_attempts)

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)
