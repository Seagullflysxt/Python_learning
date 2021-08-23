#e.g pizza.py atP97 in section6.4.2
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
print(f"You odered a {pizza['crust']} --crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
    
print(pizza['toppings'])
