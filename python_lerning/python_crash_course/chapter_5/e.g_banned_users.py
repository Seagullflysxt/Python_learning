#e.g banned users
banned_users = ['andrew','carolina','david']
user = 'marie'
user1 = 'david'

if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish")

if user1 in banned_users:
    print(f"Sorry,{user1.title()}")
    
    
