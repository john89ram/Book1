# People - Take the what you have learned from exercise 7 as well as the TIY 6.1 and make 2 more dictionaries entries of other people. 
    # Store all 3 people in a list called "people".
    # Lastly loop through the list and print all the information that was learned about them.

main_character = {'first_name': 'ashley', 'last_name': 'ramirez', 'age': 31, 'city': 'leander'}
main_character2 = {'first_name': 'jonathan', 'last_name': 'ramirez', 'age': 33, 'city': 'austin'}
main_character3 = {'first_name': 'micheal', 'last_name': 'ramirez', 'age': 9, 'city': 'cedar park'}

people = [main_character, main_character2, main_character3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    birth_place = f"{person['city']}"
    print(f"\nTHis is {full_name.title()}, and they are {person['age']} years old. They were born at {birth_place.title()}.")

print(f"It is nice to meet all of you!")