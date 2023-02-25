# 10-4 Guestbook 
    # Lets extend on what we created in 10.3 and have a while loop prompt users for names
    # When they enter their name print a greeting to the screen and add a line recording 
        # their visit in a file. Make sure each entry is in a new line.

guestbook = "Chapter10_Files_Exceptions/TIY/10.4.txt"
guest = ""
print("Hello and welcome! Please enter your name and we will save you in our guestbook.")

while True:
    user_input = input("Would you like to enter a name into the guestbook? (yes/no) ")

    if user_input == 'no':
        break

    elif user_input == 'yes':
        guest = input("What name should I save on the guestbook? ")
        with open(guestbook, 'a') as f:
            f.write(f"{guest}\n")

    else:
        print('I am sorry you can only choose "yes" or "no".')
