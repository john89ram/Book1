# First draft of function.
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

# Revised function to add middle names as well
def get_formatted_name2(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

# Another revision to correct failed test
def get_formatted_name3(first, last, middle=''):
    # Set the middle argument to nothing unless specified.
    """Generate a neatly formatted full name."""
    # Now if a middle name was added it will follow this if block
    if middle:
        full_name = f"{first} {middle} {last}"
    # of else it will remain blank and only first and last names will be counted for
    else:
        full_name = f"{first} {last}"
    return full_name.title()