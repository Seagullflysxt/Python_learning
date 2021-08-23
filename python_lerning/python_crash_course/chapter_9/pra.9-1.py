#pra.9-1 inP144
class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of this restaurant is {self.restaurant_name}.")
        print(f"The type of the cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is OPEN.")

restaurant = Restaurant('Burger King','fast food')

print(f"The restaurant's name is {restaurant.restaurant_name}.")
print(f"The cuisine's type is {restaurant.cuisine_type}.\n")


restaurant.describe_restaurant()
restaurant.open_restaurant()

res2 = Restaurant('Cheese burger','fast food')
res3 = Restaurant('Lao Wang','sea food')
res4 = Restaurant('Middle class','dang li')
res2.describe_restaurant()
res3.describe_restaurant()
res4.describe_restaurant()

