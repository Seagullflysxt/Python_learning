#pra.8-12
def make_pizzas(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizzas('pepperoni')
make_pizzas('green pepper','extra cheese','pepperoni')
make_pizzas('extra cheese','pepperoni')
    
