# Lets try a more real-world scenario - continued from part 2.
    # Now we are going to change some of the aliens to provide some excitement on our game.

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Create a for loop to grab the first 3 aliens in the list and change them to yellow aliens with all the statuses of yellow aliens.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
for alien in aliens[:5]:
    print(alien)
print("...")


print(f"Total number of aliens: {len(aliens)}")