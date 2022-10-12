# Favorite Numbers - Expand on TIY 6.2 
    # Make it so that multiple people are able to have more then one favorite number.
    # Then print each person and thier favorite number
    
# Favorite number - Create a list of people and their favorite numbers
    # This is an example of a lot of simple data for a simple subject

favorite_numbers = {
    'john': 33, 
    'ashley': [3, 7], 
    'micheal': 8, 
    'dj': 2, 
    'brooke': [7, 49]
    }

for name, num in favorite_numbers.items():
    print(f"These are {name.title()}'s favorite number(s) {num}.")