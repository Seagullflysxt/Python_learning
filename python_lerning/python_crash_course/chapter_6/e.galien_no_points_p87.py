#e.g alien no points.py p87
alien_0 = {'color':'green','points':5,'speed':'medium'}

#print(alien_0['points'])

point_value = alien_0.get('points','no point value assigned')

print(point_value)
