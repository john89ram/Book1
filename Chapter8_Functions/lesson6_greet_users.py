# Passing a list - Running a list through a function can be difficult, so 
    # lets break down how this interaction works.

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    # Just like the exercises we did in Ch4, the easiest way to print out
        # values in a list is to create a for loop.
    for name in names:
        # We create the variable "name" attach to the value 
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)