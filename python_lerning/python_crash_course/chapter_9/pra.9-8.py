#pra.9-8
class User:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is now {self.age}.")

    def greet_user(self):
        print(f"Hello,{self.first_name} {self.last_name}.")
           
class Privileges:
    def __init__(self,privileges=['can add post','can delete post','can ban user']):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Admin's privileges are as follows:")
        for self.privilege in self.privileges:
            print(f"-{self.privilege}")


class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = Privileges()


admin0 = Admin('Ada','Lovelace',49)
admin0.privileges.show_privileges()

      
