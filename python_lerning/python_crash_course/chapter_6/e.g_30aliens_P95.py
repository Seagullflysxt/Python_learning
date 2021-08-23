#30aliens.py in P95
aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

'''for alien in aliens[:5]:
    print(alien)
print("...")

print(f"The total number of aliens:{len(aliens)}.")'''


#the first 3'color change to yellow,points to 10

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
'''for alien in aliens[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast''''
     
for alien in aliens[:5]:
    print(alien)
print("...")
