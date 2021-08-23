#pra.6-8
pet_0 = {
    'type':'qiutian',
    'master':'ada',
    }
pet_1 = {
    'type':'meiduan',
    'master':'amy',
    }
pet_2 = {
    'type':'samoye',
    'master':'bob',
    }
pets = [pet_0,pet_1,pet_2]

for pet in pets:
    print(f"{pet['type'].title()}'s master is {pet['master'].title()}.")
