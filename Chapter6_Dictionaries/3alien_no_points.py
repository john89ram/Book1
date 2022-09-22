# Using the get() to access values
    # You will get an error when calling on keys that do not exist in a dictionary.
alien_0 = {'color': 'green','speed': 'slow'}
#print(alien_0['points'])

# To utilize the get() method it requires a key as a first argument. 
    # As a second (optional) arguments, you can pass the value to be returned if the key doesn't exist

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

