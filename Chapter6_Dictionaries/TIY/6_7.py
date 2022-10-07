# People - We are going to expand on TIY 6.1.
    # This time we can going to add 2 more members as separate dictionaries and then add them to a list named "people"
    # Loop through the list of people 
        # Inside the loop print all the information we have on each person

person1 = {'first_name': 'ashley', 'last_name': 'ramirez', 'age': 31}
person2 = {'first_name': 'andrew', 'last_name': 'valerio', 'age': 32}
person3 = {'first_name': 'micheal', 'last_name': 'ramirez', 'age': 9}

people = [person1, person2, person3]

for person in people:
    print(person)