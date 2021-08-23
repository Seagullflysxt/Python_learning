#pra.5-11
numbers = list(range(1,10))
ordinal_numbers = []

for number in numbers:
    print(number)

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
    
