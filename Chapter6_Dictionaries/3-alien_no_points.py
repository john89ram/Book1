# Using the get() to access values
    # You will get an error when calling on keys that do not exist in a dictionary.
alien_0 = {'color': 'green','speed': 'slow'}
#print(alien_0['points'])

# To utilize the get() method it requires a key as a first argument. 
    # As a second (optional) arguments, you can pass the value to be returned if the key doesn't exist

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Here you can see that we set the variable "point_value" to a get() method for the alien_0 dictionary.
    # It set to find the 'point' key in the dictionary, and should return the value if it was set. 
    # Since no 'point' key was created it will return "No point value assigned"

# This is a great tool to have when your code grows and you need to find if a key-value pair is missing