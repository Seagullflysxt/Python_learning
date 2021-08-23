#e.g dog inP141
class Dog:
    """A simple try to simulate a dog"""

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie',6)
your_dog = Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog's age is {your_dog.age}.")
your_dog.sit()
    
