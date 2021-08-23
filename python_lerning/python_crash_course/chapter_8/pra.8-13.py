#pra.8-13
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

user_profile = build_profile('Shi','Xiangting',
                             location = 'princeton',
                             field = 'computer science')

print(user_profile)
