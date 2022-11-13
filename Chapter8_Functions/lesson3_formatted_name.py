# Returning a simple value - Lets create a function that will return a value. 

def get_formatted_name(first_name, last_name):
    """ This function will return a titled full name. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()
    # Here we can see that the function will take in the arguments first_name and last_name
        # Then use them in the variable full name and lastly return it back with .title

# Now lets use it
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
