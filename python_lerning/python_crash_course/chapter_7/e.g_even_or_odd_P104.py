#e.g even or odd P104
number = input("Tell me a number,and I will tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\n{number} is even.")
else:
    print(f"\n{number} is odd.")
