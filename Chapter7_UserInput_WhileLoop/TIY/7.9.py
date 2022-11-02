# No Pastrami - Use TIY 7.8, and add pastrami as a sandwich to make in the order list at least 3 times.
    # Add code near the top to print that the shop has run out of pastrami 
    # Then in the while loop remove all instances of pastrami in the order

sandwich_orders = ['tuna', 'pastrami', 'ham and cheese', 'italian', 'pastrami', 
'meatball', 'club', 'pastrami']
finished_orders = []

print(f"The sandwich shop has ran out of pastrami"
"\nSorry for the inconvenience.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich.title()}")
    finished_orders.append(current_sandwich)

print(f"\nOrder up! Finished sandwich list:")
for finished_order in finished_orders:
    print(finished_order.title())