# Removing all instances of specific values from a list
    # We are going to remove all instance of a specific value

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# Here is a list of random pets that we have created.
print(pets)

while 'cat' in pets:
    # While they are 'cat's inside the list the while loop stay active
    pets.remove('cat')
    # Remove one 'cat' from the list and start over again
    
print(pets)

