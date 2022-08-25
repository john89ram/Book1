# Same as 4.1 make a list with animals with similar traits, and make a for loop to print your list
    # Mod your program to print a statement about each animal
    # Add a line at the end stating what they all have in common

animals = ['orca','lion','eagle']

print('There are plenty of animals in this world.\n\tSome are cute and cuddly and others are just not. Like:')
for animal in animals:
    print(animal.title())

print(f"\nThe {animals[0]} is the king of the seas")
print(f"The {animals[1]} is the king of the land")
print(f"The {animals[2]} is the king of the skys")

print('\nThese animals are called apex predators, and are on top of the food chain. Well other then humans...')