#moutain.py e.g inP112
responses = {}
polling_active = True

while polling_active:
    name = input("What's your name?")
    response = input("Which moutain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another people respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

print("-----Poll results-----")
for name,response in responses.items():
    print(f"{name.title()} would like to climb {response}")
    
