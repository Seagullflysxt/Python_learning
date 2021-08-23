#pra.9-15
from random import choice

sub = [1,5,0,89,20,33,73,'v','q',41,'m',50,51,'f','w']
big_suprise = []

for i in range(1,5):
    big_suprise.append(choice(sub))

print(f"Big Suprise is:{big_suprise}")

my_ticket = []
loop_go = True
nums = 0
while loop_go:
    nums += 1
    
    for m in range(1,5):
        my_ticket.append(choice(sub))
    print(f"\n{my_ticket}")
    
    if my_ticket == big_suprise:
        loop_go = False
    else:
        my_ticket = []
        
print(f"My choose is {my_ticket}.")
print(f"The loop goes for {nums} times to win the big suprise.")
#It takes so long a time!
