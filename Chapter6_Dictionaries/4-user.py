# Practicing looping through a list
    # Lets make a simple dictionary for a simple user recorded on a website

user_0 = {
    'username': 'johnram',
    'first': 'john',
    'last': 'ramirez',
}

# Now lets use a for loop to print out each element in the key: value pair
    # You will need the .items() method at the end of the for loop to address both variables key & value.
for key ,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Lets further explore this concept back in 2favorite_languages.py 
