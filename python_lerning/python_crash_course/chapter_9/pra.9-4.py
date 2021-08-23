#pra.9-4
class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"The name of this restaurant is {self.restaurant_name}.")
        print(f"The type of the cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is OPEN.")

    def reading_served(self):
        print(f"{self.number_served} people have been be served in this restaurant.")

    def set_number_served(self,nums):
        self.number_served = nums

    def increment_number_served(self,increment):
        if increment > 0:
            self.number_served += increment
        else:
            print("You can't roll back the amounts!")
    
restaurant = Restaurant('Burger King','fast food')
restaurant.reading_served()

restaurant.number_served = 99
restaurant.reading_served()

restaurant.set_number_served(100)
restaurant.reading_served()

restaurant.increment_number_served(10)
restaurant.reading_served()
