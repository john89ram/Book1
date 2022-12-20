# Keyword arguments - is a name-value pair that you pass to a function.
    # You can directly associate the name and the value within the argument
    # and this can ease confusion.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
# This will work no matter what position you place the arguments in.  