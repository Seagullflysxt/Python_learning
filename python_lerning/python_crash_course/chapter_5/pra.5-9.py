#pra.5-9
users = ['allen','amy','alice','bob','admin']
users1 = []
if users1:
    for user in users:
        if user == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print(f"Hello {user},thank you for logging again.")
else:
    print("we need to find some users!")
