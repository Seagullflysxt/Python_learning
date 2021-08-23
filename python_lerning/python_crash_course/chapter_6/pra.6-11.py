#pra.6-11
cities = {
    'shanghai':{
        'nation':'china',
        'population':'1kw',
        'fact':'fancy and modern',
        },
    'new york':{
        'nation':'america',
        'population':'2kw',
        'fact':'fancy',
        },
    'london':{
        'nation':'england',
        'population':'2.5kw',
        'fact':'beautiful',
        },
    }

for name,infos in cities.items():
    print(f"About {name.title()}:")
    print(f"Nation:{infos['nation'].title()}")
    print(f"Population:{infos['population']}")
    print(f"Fact:{infos['fact'].title()}\n")
    
