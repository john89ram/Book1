# City Names - Write a simple function called 'city_country', that takes 
    # the names of a city and its country.
    # Then have the function return a simple string format like:
    # "Santiago, Chile"

def city_country (city_name, country_name):
    """ A simple function that formats a city and its country."""
    formatted_string = f"{city_name}, {country_name}"
    return formatted_string.title()

while True:
    print(f"\nHow many cities do you know?")
    print(f"Please enter as many cities and the countries they belong to.")
    print(f"(enter 'q' at any time to quit)")
    city = input("The city: ")
    if city == 'q':
        break
    country = input("The corresponding country: ")
    if country == 'q':
        break

    formatted_string = city_country(city, country)
    print(formatted_string)