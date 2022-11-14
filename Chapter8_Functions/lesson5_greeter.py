# We are going to add on to our formatted_name function.
    # Then lets create a while loop to greet our users, and 
    # use the inputs in the loop to our function to print out a 
    # nice formal sentence greeting our users.

def get_formatted_name(first_name, last_name):
    """ This function will return a titled full name. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print(f"\nPlease tell me your name")
    print(f"(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    

