# Making an argument optional - Sometime you will need to leave some arguments optional so 
    # your function will not return an error like in this example.

# Here is the same as the previous lesson, but we added 'middle_name'
def get_formatted_name(first_name, middle_name, last_name):
    """ This function will return a titled full name. """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
    

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# However if a user does not use the middle name it will return the error we saw before.
#musician = get_formatted_name('elvis', 'presley')
#print(musician)

# So lets make the argument optional for input by setting its default value null.

def get_formatted_name(first_name, last_name, middle_name=''):
    # We save middle_name for last as it might cause an error in your editor
        # But we set the default value to null by not entering anything in the ' '
    """ This function will return a titled full name. """
    # Created a simple if statement so we can get a correct format of our requested name.
        # If we did not there would be an extra space added in between the first and last names. 
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Lets try this once more and see what we get.
musician = get_formatted_name('elvis', 'presley')
print(musician)