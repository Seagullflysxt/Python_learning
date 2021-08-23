#pra.7-8
sandwich_orders = ['tuna sandwich','cemita','tripleta']
finished_sandwiches = []

for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order}.")
    finished_sandwiches.append(sandwich_order)

print("\nThe following sandwiches have been made for you:")
for finished_sandwich in finished_sandwiches:
    print("\t"+finished_sandwich)
    
