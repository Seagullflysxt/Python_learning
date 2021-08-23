#pra.6-5
important_river = {
    'nile':'eygpt',
    'amozan river':'brazil',
    'changjiang river':'china',
    }
for river,country in important_river.items():
    print(f"The {river.title()} runs through {country.title()}.")
    
for river in important_river.keys():
    print(river.title())

for country in important_river.values():
    print(country.title())
