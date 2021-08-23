'''#e.g6.2.3alien.py at p84top
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)'''


#e.g6.2.4alien.py atp84
'''alien_0 = {'color':'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")'''

#alien_speed.py
'''print(f"The original position is {alien_0['x_po']}.")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_po'] = alien_0['x_po']+x_increment

print(f"New position is {alien_0['x_po']}.")'''


#e.g6.2.5 alien.py at p85
alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['color']
print(alien_0)
