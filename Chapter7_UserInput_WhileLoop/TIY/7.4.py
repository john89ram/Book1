# Pizza toppings - Create a program for users to enter as many pizza toppings until they enter 'quit'
    # After each topping print that you will add that topping to the pizza

pizza_toppings = []
active = True

print(f'Please enter all the toppings you would like on your pizza.'
    '\nWhen you are finished type "quit": ')

while True:
    message = input("Topping: ")
    if message == 'quit':
        break

    print(f"Ok, we will add {message} to your pizza.")
    pizza_toppings.append(message)

print("Your pizza has the following toppings:")
for pizza_topping in pizza_toppings:
    print(f"{pizza_topping},")
print("Thank you, have a great day!")