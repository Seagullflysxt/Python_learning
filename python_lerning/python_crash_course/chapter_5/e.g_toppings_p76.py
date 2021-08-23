#e.g toppings.py at p76
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinshed making your pizza!")
