# Using a wildcard '*' as an argument in a function
    # You might have to change the number of arguments in a function 
    # luckily you can use the * to pass as many of them as needed.

def make_pizza(*toppings):
    """
    Print the list of toppings that have been requested
    """
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese',)