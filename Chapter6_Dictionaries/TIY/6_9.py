# Favorite places - 
    # Ashley, Torchy's, tacos
    # DJ, Park, fun place to play
    # Micheal, tacocabana, delicious tortilla 
    # john, the oasis, amazing views
    
favorite_places = {
    'ashley': "torchy's",
    'dj': 'parks',
    'micheal': 'tacocabana',
    'john': 'the oasis'
    }

for name, place in favorite_places.items():
    print(f"{name.title()}'s favorite place to go is {place.title()}.")