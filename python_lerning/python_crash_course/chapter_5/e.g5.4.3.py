#e.g.5.4.3 at p78
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"sorry,we don't have {requested_topping}")

