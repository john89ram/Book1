# Checking Usernames - Do the following to create a program that simulates how a website ensures that everyone has a unique username
    # Make a list of 5 or more users called "current_users"
    # Make another list of five or more users called "new_users". Make sure 2 users are apart of the "current_list" as well.
    # Loop through the "new_users" list to see if each new username has already been used. 
        # If is has been used print "Enter another username"
        # If it has not been used print "This username is available".
    # Make sure the comparison is case insensitive. If John has been used JOHN/JOhn/JOHn etc can not be used.

current_users = ['john','dj','michael','ashley','mocha']
new_users = ['DJ','Mocha','mary','susan','BROOKE']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Enter another username")
    else :
        print("This username is available")
