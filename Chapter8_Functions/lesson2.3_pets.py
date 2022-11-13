# Argument errors - You might run into errors if not enough argument are provided for the function to do its job.

def describe_pet(pet_name, animal_type):
    # Lets just set the basic parameters.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Now when we run the function without any arguments you should get an error code.

describe_pet()