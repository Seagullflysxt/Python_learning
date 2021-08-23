#e.g many_users.py in p99 in 6.4.3
users = {
    'aeinstein':{
        'first':'albert',
        'last':'aeinstein',
        'location':'princeton',
        },
    
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for user_name,user_info in users.items():
    print(f"User name:{user_name}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"Full name:{full_name.title()}")
    print(f"Location:{location.title()}")
