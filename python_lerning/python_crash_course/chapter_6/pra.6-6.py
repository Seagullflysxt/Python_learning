#PRA.6-6
fav_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'java',
	'phil':'ruby',
	}

for name,language in fav_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

uncertain_name = ['bob','alice','jen']

for name in uncertain_name:
    if name in fav_languages.keys():
        print(f"Thank you,{name.title()}.")
    else:
        print(f"{name.title()},please take in our poll.")
        
    
