# 10-12 Favorite number remembered
    # Combine the 2 files you created in 10.11 into one program
    # Also program to prompt the user for their favorite number if it was not saved

import os
import json

os.chdir("Chapter10_Files_Exceptions/TIY/")

def remember_num():
    """A function to retrieve the users favorite number"""
    filename = 'fav_num.json'
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        return fav_num
    
def get_num():
    """Function to request a favorite number from the user."""
    fav_num = input("What is your favorite number? ")
    filename = 'fav_num.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
    return fav_num

def favorite_number():
    """Saving or displaying users favorite number"""
    fav_num = remember_num()
    if fav_num:
        print(f"I know your favorite number! It is {fav_num}.")
    else:
        fav_num = get_num()
        print(f"We will remember your favorite number for next time.")

favorite_number()