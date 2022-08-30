# Checking whether a value is not in a list, use the 'not in' argument in you if statement;
banned_users = ['andrew','carolina','david']
user = 'marie'
#-------- \/ (Here the 'not in' argument ask Python to check the list and perform a function whether it is true or not)
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
else:
    print(f"Sorry {user.title()}, you have been banned.")
