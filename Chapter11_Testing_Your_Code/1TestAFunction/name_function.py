import os

os.chdir('Chapter11_Testing_Your_Code/1TestAFunction/')

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()

