# Dictionary of similar objects
    # You can create all types of dictionaries (One item with a lot of attributes or even one subject with a lot of ppl.)
    # Create a pool of ppl and their favorite programming language

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': "python"
}
# Now lets print out the favorite language of someone within the poll
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#-------------------- Continue after 4user.py --------------------------
    
# Now we're going to take what we learned in 4user.py and use it to make our code more dynamic.

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Now that we able to print both key, value pairs, lets try to print just the names of this group.

for name in favorite_languages.keys():
    print(name.title())