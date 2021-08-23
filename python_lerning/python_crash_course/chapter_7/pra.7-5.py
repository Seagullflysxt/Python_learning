#pra.7-5
message = "How old are you?"

while True:
    age = input(message)
    age = int(age)
    if 0 < age < 3:
        print("Free")
    elif age <= 12:
        print("10$")
    else:
        print("15$")
    

     
