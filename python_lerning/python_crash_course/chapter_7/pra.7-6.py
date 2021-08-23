#pra.7-6
#using if in while
prompt = "\nPlease enter some toppings for your pizza:"
prompt += "\nEnter 'quit' to finish adding toppings."

message = ' '

'''while message != 'quit':
    topping = input(prompt)
    if topping == 'quit':
        print(f"Adding toppings finished.")
    else:
        print(f"We will add {topping} in your pizza.")'''

#using break
while message != 'quit':
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"\nWe will add {topping} to your pizza.")   #running nice

