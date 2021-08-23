#pra.7-9
sandwich_orders = ['tuna sandwich','pastrami','cemita','pastrami','pastrami','tripleta']
print(sandwich_orders)

print("Pastrami sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

if 'pastrami' not in sandwich_orders:
    print("Pastrami sold out confirmed.")
else:
    print("Pastrami still in stock.")
