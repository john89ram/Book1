# 10-13 Verify User
    # Take the final code from remember_me.py and we are going to add a verification script
    # We are going to ask the user to confirm or not the saved username is them or not.
    # If not we will run the get_new_username() and write over what was saved.

import os
import json

os.chdir("Chapter10_Files_Exceptions/TIY/")

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        verification = input(f"Are your {username}?(Enter y/n) ")
        if verification == 'y':
            return username
        else:
            return None

def get_new_user():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user()
        print(f"We will remember you when you come back, {username}!")

greet_user()