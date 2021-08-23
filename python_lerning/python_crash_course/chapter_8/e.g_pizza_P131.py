#e.g pizza.py inP131
'''def make_pizzas(*toppings):
    print(toppings)

make_pizzas('pepperoni')
make_pizzas('mushrooms','green peppers','extra cheese')'''


'''def make_pizzas(*toppings):
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings:
        print(f"-{topping}")

make_pizzas('pepperoni')
make_pizzas('mushrooms','green peppers','extra cheese')'''


#make pizzas with index size

def make_pizzas(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizzas(16,'pepperoni')
make_pizzas(12,'mushrooms','green pepper','extra cheese')
