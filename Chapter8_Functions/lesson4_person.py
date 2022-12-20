# Returning a dictionary - functions can also store and return dictionary information.
    # Lets create a simple function that explores this concept.

def build_person(first_name, last_name):
    """This function will take basic information for a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print = musician
