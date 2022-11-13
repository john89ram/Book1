# Default values - Functions can have default values set so no arguments need to be entered.
    # They can be overwritten if enter the full keyword pair.

def describe_pet(pet_name, animal_type='dog'):
    # Be sure if a default value is used to put it in the end of the parameter list.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('Willie')
describe_pet(pet_name='Harry')
describe_pet(pet_name='Harry', animal_type='hamster')

# Equivalent function calls - You can also call by parameter location as well without needing to list the keyword value.
describe_pet('james', 'lizard')