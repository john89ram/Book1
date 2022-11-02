# Dream Vacation - Write a program that polls users about their dream vacay
    # Write a prompt to ask them for their name and where they would go.
    # At the end print the results.

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where would you like to go on vacation? ")
    
    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/ n) ")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to go to {response} for a vacation trip.")
