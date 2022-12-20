# Mixing positional and arbitrary arguments - sometimes you need to add both positional arguments along with arbitrary ones. Let see how these functions are supposed to be configured. Lets use the pizza function that we created earlier in lesson 8.

def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Now we can see that we have both used in this function. Lets test it out.

make_pizza(12, "pepperoni")
make_pizza(16, "mushrooms", "green peppers", "extra cheese")