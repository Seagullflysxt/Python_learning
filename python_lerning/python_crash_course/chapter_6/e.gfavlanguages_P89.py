#e.g favorite_languages P89
fav_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'java',
	'phil':'ruby',
	}

#########.keys()
'''for name,language in fav_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in fav_languages.keys():
    print(name.title())'''

    
#P91
'''friends = ['phil','sarah']

for name in fav_languages.keys():
    print(f"Hi,{name.title()}.")

    if name in friends:
        language = fav_languages[name].title()
        print(f"\t{name.title()},I see you love {language}.")
        
if 'erin' not in fav_languages.keys():
    print("\nErin,please take our poll!")'''

#P92
'''for name in sorted(fav_languages.keys()):
    print(name.title())'''

#########.values()


#6.3.4 P92-P93
print("The following languages have been mentioned:\n")
for language in set(fav_languages.values()):
    print(language.title())
