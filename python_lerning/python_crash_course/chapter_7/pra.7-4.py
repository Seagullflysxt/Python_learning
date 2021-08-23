#pra.7-4
message = "\nPlease enter some toppings for your pizza:"
message += "\nEnter 'quit' to finish adding toppings."

add_active = True

while add_active:
    toppings = input(message)
    if toppings != 'quit':
        print(f"\nWe will add {toppings} in your pizza.")
    elif toppings == 'quit':
        add_active = False
