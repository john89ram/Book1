# 10-11_part1 Favorite number
    # Write a program that prompts the user for a favorite number.
    # Use json.dump to store the number in a file.
    # In part 2 write a program to read the saved file.
        # and prints "I know your favorite number! Its [number]"

import os
import json

os.chdir("Chapter10_Files_Exceptions/TIY/")

filename = 'fav_num.json'

with open(filename) as f:
    fav_num = json.load(f)
    print(f"I know your favorite number! Its {fav_num}.")