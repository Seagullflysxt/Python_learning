#e.g greeter.py inP125
'''def get_formatted_name(first_name,last_name):
    #return formatted name
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("First_name:")
    l_name = input("Last_name:")

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"Hello,{formatted_name}!")'''


#greeter with easy exit
def get_formatted_name(first_name,last_name):
    #return formatted name
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    
    f_name = input("First_name:")
    if f_name == 'q':
        break
    l_name = input("Last_name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello,{formatted_name}!")
