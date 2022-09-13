# Hello Admin - Make a list of five or more usernames, including the name 'admin'. 
    # Write a code that will greet each each user after they log into a website.
    # If the user is the admin print a special message "Hello admin, would you like a status report?"
    # Otherwise a generic greeting of "Hello {user}, thank you for logging in again."

admin_users = ['admin','john']
users = ['ashley','dj','michael','john']

for user in users:
    if user in admin_users:
        print(f"Hello {user.title()}, would you like a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")