#pra.5-8
users = ['allen','amy','alice','bob','admin']
for user in users:
    if user == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {user},thank you for logging again.")
