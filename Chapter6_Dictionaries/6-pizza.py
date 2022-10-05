# List in a Dictionary - Sometimes there are times you need to expand description on keys or add toppings on a pizza
    # Lets create a pizza that is a bit more complicated

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Lets confirm the pizza order with the customer
print(f"Does this order look right:\nOne {pizza['crust']} pizza with the following toppings.")

for toppings in pizza['toppings']:
    print(toppings)

print("Is this correct?")
