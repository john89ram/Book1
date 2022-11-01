# Deli - Make a list called sandwich_orders and fill it with the names of various sandwiches.
    # Then make an empty list called finished_sandwiches. 
    # Loop through the list of sandwich orders and print a message for each order
        # such as "I made your {sandwich} sandwich."
    # As each sandwich is made move it from orders to finished list
    # At the end make a final list of the orders

sandwich_orders = ['tuna', 'ham and cheese', 'italian', 'meatball', 'club']
finished_orders = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich.title()}")
    finished_orders.append(current_sandwich)

print(f"\nOrder up! Finished sandwich list:")
for finished_order in finished_orders:
    print(finished_order.title())