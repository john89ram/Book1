# A simple dictionary holding information of an aliens color and point value.
alien_0 = {'color': 'green', 'points': 5}

# Now lets print the elements that this variable holds.
print(alien_0['color'])
print(alien_0['points'])

#--------------------- *** Example of how to call a key-value pair ***

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#--------------------- *** Adding key-value pairs to a dictionary ***

alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)

#--------------------- *** Starting with an empty dictionary ***
del alien_0

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 0

print(alien_0)

#--------------------- *** Modifying a dictionary key ***

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}!")

# Lets try something a little more complicated and program this alien to move a bit. (With different speeds.)

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")

    # Move the alien to the right
    # Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 'fast' alien 
    x_increment = 3

# Lets add the aliens speed to its current position to make it move
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Deleting values from dictionaries
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)