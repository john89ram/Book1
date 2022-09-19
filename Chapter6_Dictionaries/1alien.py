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

