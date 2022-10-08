# Pets - We are going to make several dictionaries over the pets in your life.
    # They are going to include any information that you remember about them. 
    # Put them all in a list called my_pets
    # Then were going to create a for loop and introduce our pets and what you remember about them.

pet_1 = {'name': 'sabrina', 'type': 'cat','color': 'calico','gender': 'she', }
pet_2 = {'name': 'justin', 'type': 'cat','color': 'black and white','gender': 'he', }
pet_3 = {'name': 'mocha', 'type': 'dog','color': 'brown and black','gender': 'she', }
pet_4 = {'name': 'missy', 'type': 'dog','color': 'black','gender': 'she', }

my_pets = [pet_1, pet_2, pet_3, pet_4]

for pet in my_pets:
    pet_name = f"{pet['name']}"
    gender_start = f"{pet['gender']}"
    print(f"\nThis is {pet_name.title()}. {gender_start.title()} is a {pet['color']} {pet['type']}.")