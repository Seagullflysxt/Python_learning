#e.g printing_models.py inP128
'''unprinted_models = ['phone case','robot pendant','dodecahedron']
completed_models = []

while unprinted_models:
    current_design = unprinted_models.pop()
    print(f"Printing model:{current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)'''


#build 2 functions
def print_models(unprinted_designs,completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model:{current_design}")
        completed_designs.append(current_design)

def show_completed_models(completed_designs):
    for model in completed_designs:
        print(model)

unprinted_models = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_models[:],completed_models)
print("\nThe following models have been printed:") 
show_completed_models(completed_models)
print(unprinted_models)


