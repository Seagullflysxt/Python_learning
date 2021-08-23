#person.py inP124
'''def build_person(first_name,last_name):
    #return a dictionary which includes a man's info
    person = {'first':first_name,'last':last_name}
    return person

musician =build_person('jimi','hendrix')
print(musician)'''




#person with age inP125
def build_person(first_name,last_name,age = None):
    #return a dictionary which includes a man's info
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    
    return person

musician =build_person('jimi','hendrix')
print(musician)
musician = build_person('john','hooker',27)
print(musician)
