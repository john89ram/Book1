# Dice - Make a class die with one attribute called sides which is default 6
    # Write a method called roll_dice() that prints a random number between the side value.
    # Roll this die 10 times then change the sides to 10 and roll again, and then 20 and etc.
from random import randint

class Die:
    """A simple representation of a single die"""
    
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_dice(self):
        """Represents a roll of the die"""
        lucky_number = randint(1, self.sides)
        return lucky_number
    
num_roll = range(10)

# 6 sided die
six_sides = Die()
# Roll
print(f"\n6 sided die numbers:")
for num in num_roll:
    print(six_sides.roll_dice())

# 10 sided die
ten_sides = Die(10)
# Roll
print(f"\n10 sided die numbers:")
for num in num_roll:
    print(ten_sides.roll_dice())
    
# 20 sided die
twenty_sides = Die(20)
# Roll
print(f"\n20 sided die numbers:")
for num in num_roll:
    print(twenty_sides.roll_dice())