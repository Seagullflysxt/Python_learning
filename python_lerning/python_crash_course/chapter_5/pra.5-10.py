#pra.5-10
'''current_users = ['allen','alice','bob','amy','hanya']
new_users = ['dave','amy','danti','linya','alice']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} has been used,try another one.")
    else:
        print(f"{new_user} hasn't been used.")'''

#pra.5-10.4 differ capitalization or lowercase
current_users = ['Allen','Alice','Bob','amy','Hanya']

current_duplicate_low = []
for current_user in current_users:
    current_duplicate_low.append(current_user.lower())     #duplication in lowercse

print(current_duplicate_low)   # duplication created sucssefully 
print("\n")

new_users = ['dave','Amy','danti','linya','alice']
for new_user in new_users:
    if new_user.lower() in current_duplicate_low:
        print(f"{new_user} has been used,try another one.")
    else:
        print(f"{new_user} hasn't been used.")    #bingo!
