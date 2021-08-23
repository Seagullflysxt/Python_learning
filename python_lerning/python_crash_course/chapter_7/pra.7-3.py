#pra.7-3
num = input("Please enter a digit:")
num = int(num)

if num == 0:
    print("No...")
elif num % 10 == 0:
    print("Yes.")
else:
    print("No.")
