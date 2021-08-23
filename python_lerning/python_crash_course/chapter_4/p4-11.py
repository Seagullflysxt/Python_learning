#PRACTICE4-11
my_pizzas = ['pizzaolo','pizza napoletana','margherita']

friend_pizzas = my_pizzas[:]   #creat a duplicate

my_pizzas.append('pizza hut')
friend_pizzas.append('papaJohns')

print("\nmy favorite pizzas are:")
print(my_pizzas)

print("\nfriend pizzas are:")
print(friend_pizzas)
print("\n")

for pizza in friend_pizzas:
    print(pizza)
