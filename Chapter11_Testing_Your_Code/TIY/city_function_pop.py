# 11-2 Population
    # Modify the code in 11.1 to have a third parameter: population
    # The final product to be as follows: "Santiago, Chile - population xxx"
    # Reconfigure the test to reflect what is desired above
        # Run the test, the first test should fail as we have not have not shown the program how to deal with population being optional
        # Modify the function to make population optional
        # Test once more to get a pass.

def city_country_pop(city, country, population):
    """A function that properly formats city and country names"""
    formatted_names = f"{city}, {country} - population {population}"
    return formatted_names.title()

#------------------------------------------------------------------------------------------------------------------------

# Now lets configure this function to make population an optional parameter

def city_country_pop2(city, country, population=''):
    """A function that properly formats city and country names"""
    if population:
        formatted_names = f"{city}, {country} - population {population}"
    else:
        formatted_names = f"{city}, {country}"
    return formatted_names.title()
