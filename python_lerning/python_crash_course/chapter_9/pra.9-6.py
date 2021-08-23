#pra.9-6
class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of this restaurant is {self.restaurant_name}.")
        print(f"The type of the cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is OPEN.")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['watermelon','peach','pear']

    def show_flavors(self):
        print("Flavors are as follows:")
        for self.flavor in self.flavors:
            print(f"-{self.flavor}")

icecreamstand = IceCreamStand('McDonulds','fast food')
icecreamstand.show_flavors()
