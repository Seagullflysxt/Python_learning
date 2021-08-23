#e.g favlanguages in P98
fav_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }

for name,languages in fav_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is {name.title()}.")
    else:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print("\t\t"+language.title())
