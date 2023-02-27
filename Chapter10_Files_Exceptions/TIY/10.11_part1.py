# 10-11_part1 Favorite number
    # Write a program that prompts the user for a favorite number.
    # Use json.dump to store the number in a file.
    # In part 2 write a program to read the saved file.
        # and prints "I know your favorite number! Its [number]"

import os
import json

os.chdir("Chapter10_Files_Exceptions/TIY/")

filename = 'fav_num.json'

fav_num = input("What is your favorite number? ")

with open(filename, 'w') as f:
    json.dump(fav_num, f)
    print("Thank you, I will remember that for next time.")
    