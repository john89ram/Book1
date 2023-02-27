# 11-1 City, Country
    # Create a function that accepts two parameters: a city name and a country name.
    # The function then should return a single string in the form of "City, Country"
        # Ex. "city, country" -> "City, Country"
    # Then we will create a test Class to test our function.

def city_country(city, country):
    """A function that properly formats city and country names"""
    formatted_names = f"{city}, {country}"
    return formatted_names.title()