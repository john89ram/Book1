# Let create a simple module that saves our functions to be called at a later date.
    # Here we have our simple pizza function from lesson 8.
    # Lets save it here in the modules folder and call on it in another program.

def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
