import os
import json

os.chdir("Chapter10_Files_Exceptions/4StoringData/")


#---------------------------------------------------------------------------------------------------

### Saving and reading User-generated data (Part 1) ###

# 'filename' is NEEDED for this script and the one right below, but not for the last!!!!
#filename = 'username.json'

#username = input("What is your name? ")
#with open(filename, 'w') as f:
#    json.dump(username, f)
#    print(f"We will remember you when you come back, {username}!")

#---------------------------------------------------------------------------------------------------

# Piecing both parts 1 and 2 into a single code block

#try:
#    with open(filename) as f:
#        username = json.load(f)
#except FileNotFoundError:
#    username = input("What is your name? ")
#    with open(filename, 'w') as f:
#        json.dump(username, f)
#        print(f"We will remember you when you come back, {username}!")
#else:
#    print(f"Welcome back, {username}!")

#---------------------------------------------------------------------------------------------------

### Refactoring ###

# Refactoring is when it might be easier to break your code into different parts 
    # Lets try to break down the try block above into different functions

#def get_stored_username():
#    """Get stored username if available."""
#    # Same code as we usually know. 
#    filename = 'username.json'
#    try:
#        with open(filename) as f:
#            username = json.load(f)
#    # Silent error catch, and return nothing back 
#    except FileNotFoundError:
#        return None
#    # Added to this just in case the file was not deleted but the data inside was. 
#    except json.decoder.JSONDecodeError:
#        return None
#    # If username is found it will be returned back.
#    else:
#        return username
#    
#def greet_user():
#    """Greet the user by name."""
#    # Function call to find stored names in our json file
#    username = get_stored_username()
#    if username:
#        print(f"Welcome back, {username}!")
#    # The return of None will trigger this else block and will request a name and save it to the json file.  
#    else:
#        username = input("What is your name? ")
#        filename = 'username.json'
#        with open(filename, 'w') as f:
#            json.dump(username, f)
#            print(f"We will remember you when you come back, {username}!")
#
#greet_user()

#---------------------------------------------------------------------------------------------------

# Lets break it down once more so each function has its own clear task

# Still the same nothing changed as it already has a clear and simple task.
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
        return username
   
# We took the end of the else block on the code above and created a new function to ONLY create a new user.
def get_new_user():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

# Now greet_user() will ONLY greet the user and if there is more work to be done it will call the other functions to handle the work and return its values.
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user()
        print(f"We will remember you when you come back, {username}!")

greet_user()