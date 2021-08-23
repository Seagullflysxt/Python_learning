#pra.6-7
people_0 = {
    'first':'ada',
    'last':'lovelace',
    'age':39,
    'city':'london',
    }
people_1 = {
    'first':'bob',
    'last':'dylon',
    'age':70,
    'city':'boston',
    }
people_2 = {
    'first':'john',
    'last':'lenon',
    'age':70,
    'city':'liverpool',
    }

peoples = [people_0,people_1,people_2]

for people in peoples:
    print(f"Full name:{people['first'].title()} {people['last'].title()}")
    print(f"Age:{people['age']}")
    print(f"City:{people['city'].title()}")
    print("\n")
