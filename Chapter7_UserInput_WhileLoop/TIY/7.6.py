# Three Exits - Write a different version of TIY 7.4 or 7.5 but include the following requirements:
    # Use a conditional test in a while statement to stop the loop
    # Use an active variable to control how long the loop runs
    # Use a break statement to exit the loop when the user enters 'quit'

pizza_toppings = []
topping_count = 0
active = True

print(f'Please enter at least 3 toppings you would like on your pizza.'
    '\nWhen you are finished type "quit": ')

while active:
    message = input("Topping: ")
    if message == 'quit':
        break
    elif message == 'pineapple':
        print(f"I am sorry but pineapple is not a topping!")
        continue
    elif  topping_count == 2:
        active = False
    print(f"Ok, we will add {message} to your pizza.")
    topping_count += 1
    pizza_toppings.append(message)

print("Your pizza has the following toppings:")
for pizza_topping in pizza_toppings:
    print(f"{pizza_topping},")
print("Thank you, have a great day!")