# Dictionary of similar objects
    # You can create all types of dictionaries (One item with a lot of attributes or even one subject with a lot of ppl.)
    # Create a pool of ppl and their favorite programming language

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
# Now lets print out the favorite language of someone within the poll
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#-------------------- Continue after 4user.py --------------------------
    
# Now we're going to take what we learned in 4user.py and use it to make our code more dynamic.

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Now that we able to print both key, value pairs, lets try to print just the names of this group.
    # The .key() method is a formality, however it is default and is not required to have it to work properly.
for name in favorite_languages.keys():
    print(name.title())

# Now lets get a little more complicated and mix in an if statement as well
    # Create an if state to call out to a friend while greeting the rest of the group.

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    # This is the same script as the previous but we are just greeting all members in the dictionary.
    # ----------*** Warning be sure the if statement is indented with the for loop or you will run into issues.
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")
    
    # Here inside the for loop we ask if there are any 'friends' within the group
        # If there are, python will assign their language inside the dictionary to a variable to be used later in the code
        # Lastly once the friend is found the code will print an additional sentence and use the key(name),
            # as well as the value(language) from the dictionary.

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Now lets learn how to loop through a dictionary in particular orders
    # Lets mix our sort() method and see what happens

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    # Here we sorted the favorite_languages dictionary (only the keys)
        # Then we printed every name with the title format, and thanked them.

# Next lets loop through the values

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    # As you can see Python was chosen twice, this can be annoying when dealing with huge data sets, lets fix that

# When only looking for unique sets use the set() method
for language in set(favorite_languages.values()):
    print(language.title())
    # Much cleaner - clean code is always appreciated 