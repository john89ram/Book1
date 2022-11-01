# Moving items from one list to another list. 

# Start with users that need to be verified.
    # and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
    # Move each verified user into the list of confirmed users.

while unconfirmed_users:
    # This while loop will run as long as the list is not empty.
    current_user = unconfirmed_users.pop()
    # This sets a new variable called "current_user" which is = to 
        # .pop which is the last person on the list and removes it from that list.

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    # Here sims how it would look like when a website is verifying a user
        # Then we take the "current_user" and append it to the end of the "confirmed_users"

print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#This part will display all "confirmed_users" that were transferred.