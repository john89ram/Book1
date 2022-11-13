# Cities - Write a function called describe_city() that have the parameters 'city_name' and
    # and its 'country'. This function should print a simple sentence, like "Reykjavik is in Iceland."
    # Give the parameter for the country a default value. Call your function 3 times with 3 different cities, 
    # and at least once in a different country.

def describe_city(city_name, country='United States of America'):
    """This function will print a simple sentence with a city and the country it belongs to."""

    print(f"\nThe city of {city_name.title()} resides in {country.title()}.")

describe_city('austin')
describe_city(city_name='san antonio')
describe_city('amsterdam', country='Netherland')