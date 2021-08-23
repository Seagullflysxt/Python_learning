#e.g amusement.py
'''age = 12

if age <4:
    print("free")
elif age <18:
    print("Your admission cost is 25$")
else:
    print("Your admission cost is 40$")'''

#optimization
'''age = 12

if age <4:
    price = 0    
elif age <18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")'''

#halfprice for those who is older than 65
'''age = 67

if age <4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")'''

#no else: used
age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

