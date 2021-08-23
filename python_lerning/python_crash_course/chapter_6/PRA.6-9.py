#pra.6-9
favorite_places = {
    'ada':['london','parice','boston'],
    'amy':['london','new york','boston'],
    'bob':['liverpool','boston','parice'],
    }
for name,places in favorite_places.items():
    print(f"{name.title()}'s favorite places:")
    for place in places:
        print(F"\t{place.title()}")
