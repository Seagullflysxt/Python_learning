#pra.6-10
fav_numbers = {
    'ada':[3,2,1],
    'amy':[33,22],
    'alice':[1,99],
    'bob':[2,98],
    'dave':[23,77],
    }
for name,numbers in fav_numbers.items():
    print(f"{name.title()}'s favorite numbers:")
    for number in numbers:
        print(f"\t{number}")
