#pra.9-13
from random import randint
class Die:

    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        side = randint(1,self.sides)
        print(side)

dice_6 = Die()
dice_6.roll_die()
print("Now give a 10 times try:")
for i in range(1,11):
    dice_6.roll_die()
    
dice_10 = Die(10)
dice_20 = Die(20)

print("\nFor dice_10:")
for i in range(1,11):
    dice_10.roll_die()
    
print("\nFor dice_20:")
for i in range(1,11):
    dice_20.roll_die()

