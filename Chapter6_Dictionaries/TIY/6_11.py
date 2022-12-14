# Cities - Make a dictionaries called "cities". Use the name of 3 cities as keys. 
    # Create a nested dictionary inside for the values of the cities.
    # Inside input info over these cities (country, population, and an interesting fact)
    # Print each city and the facts that discovered for each.
    
cities = {
    'ontario': {
        'country': 'canada',
        'population': 14_570_000,
        'fact': "known for Parliament Hill's Victorian architecture and the National Gallery",
        }, 

    'austin': {
        'country': 'america',
        'population': 965_872,
        'fact': 'known as the live music capital of the USA',
        },

    'hot springs': {
        'country': 'america',
        'population': 38_697,
        'fact': 'known for naturally heated springs',
        },
}

for city, city_info in cities.items():
    country = city_info['country']
    pop = city_info['population']
    fact = city_info['fact']
    print(f"\nIn {country.title()}, {city.title()} they have a population of {pop}. One interesting fact about {city.title()}, is that they are {fact}.")