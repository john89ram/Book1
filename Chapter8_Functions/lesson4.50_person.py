# Functions can store all types of not just simple strings. It can 
    # also process and return complicated data types as well. 
    # For now lets just try to add age to our previous function.

def build_person(first_name, last_name, age=None):
    # Here we have an optional parameter for age, and set it to none.
    """ This function will take basic information for a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    # As in lesson 3 we used an if statement to add age to the dictionary.
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
