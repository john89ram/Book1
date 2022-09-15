# No users - Add an if test to hello_admin (5_8.py) to make sure the list of users is not empty 
    # If the list is empty, print the message "We need to find some users!"
    # Remove all users from the list to test your new condition

admin_users = ['admin','john']
users = ['ashley','dj','michael','john']

if len(users) > 0:
    for user in users:
        if user in admin_users:
            print(f"Hello {user.title()}, would you like a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")