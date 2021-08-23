#pra.7-10
dream_places = {}

polling_active = True

while polling_active:
    name = input("What's your name?")
    place = input("If you could visit one place in the world,where would you go?")

    dream_places[name] = place

    repeat = input("would you like to let another to join in this polling?(yes/no)")
    if repeat == 'no':
        polling_active = False
        
print("\n")    
for name,place in dream_places.items():
    print(f"{name.title()} would like to go {place.title()}.")
