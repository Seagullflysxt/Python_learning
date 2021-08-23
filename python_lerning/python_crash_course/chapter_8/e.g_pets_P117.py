#e.g pets.py inP117
'''def describe_pet(animal_type,pet_name):
    #display pet's info
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')

#e.g pets.py inP119
def describe_pet(animal_type,pet_name):
    #display pet's info
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster',pet_name = 'harry')
describe_pet(pet_name = 'harry',animal_type = 'hamster')'''




#e.g pets.py inP120
def describe_pet(pet_name,animal_type = 'dog'):
    #display pet's info
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'harry')
describe_pet('harry')
describe_pet(pet_name = 'willie',animal_type = 'hamster')
#describe_pet()   #missing 1 required possitional argument
