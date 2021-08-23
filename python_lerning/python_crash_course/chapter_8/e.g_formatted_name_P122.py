#foformatted_name.py inP122
'''def get_formatted_name(first_name,last_name):
    #return formatted name
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')

print(musician)'''


#formatted_name with middle name

def get_formatted_name(first_name,last_name,middle_name = ''):
    #return formatted name with middle name
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)
