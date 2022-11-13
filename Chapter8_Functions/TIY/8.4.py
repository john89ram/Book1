# T-shirt modified - Create a function called make_shirt() with the parameters 'size' and 'text'.
    # With default values of size = large and text = "I love python"
    # The function should print a sentence that will overview the order of the shirt's size and
    # the message ('text') that should be printed on the shirt.

def make_shirt(size= 'large', text= 'I love python!'):
    """The function should print a sentence that will overview the order of the shirt's size and,"""
    """the message ('text') that should be printed on the shirt."""

    print(f'\nYou have ordered a {size} shirt, with "{text}" printed.')

# Lastly print different various orders from the default.

make_shirt()
make_shirt('small', 'TACO TUESDAY!')
make_shirt(text="I'm with stupid")
make_shirt(size='XL', text='BIG PAPA')