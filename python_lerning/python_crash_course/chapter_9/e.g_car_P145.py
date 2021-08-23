# e.g car.py in P145
class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
            
'''my_new_car = Car('audi','a4',2019)
#my_new_car.year = 2020
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
#my_new_car.odometer_reading = 30
my_new_car.read_odometer()
my_new_car.update_odometer(19)
my_new_car.read_odometer()'''
my_used_car = Car('subaru','outack',2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()
