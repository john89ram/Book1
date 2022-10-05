# Nesting - is storing multiple dictionaries in a list, or a list of items as a value in a dictionary. (ex. Dict in List, List in Dict, or even Dict in Dict)
    # First up, lets create a list of dictionaries.

alien_0 = {'color': 'green','points': '5'}
alien_1 = {'color': 'yellow','points': '10'}
alien_2 = {'color': 'red','points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
