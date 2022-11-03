# Positional Arguments
    # Lets practice with multiple parameters and position

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# Take care of the position of the arguments as they can be easily mixed up
describe_pet('sharkbait', 'fish')
# This can be resolved by using keyword arguments in the next part of this lesson.