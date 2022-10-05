# Lets try a more real-world scenario
    # Lets create a program to create these aliens for us, we will utilize the range() method to create these aliens

# Lets start with an empty list of aliens.
aliens = []

# Now lets make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")