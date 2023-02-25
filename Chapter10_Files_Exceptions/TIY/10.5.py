# 10-5 Programming Poll
    # Write a while loop that asks ppl why they like programming.
    # Each time someone enters a reason, add their reason to a file that stores the responses

program_poll = "Chapter10_Files_Exceptions/TIY/10.5.txt"
poll_results = ""

print("Hello! We are taking a quick poll and asking ppl why they like programming.")

while True:
    user_input = input("Would you like to take part in our poll? (yes/no) ")

    if user_input == 'no':
        break

    elif user_input == 'yes':
        poll_results = input("What do you enjoy about programming? ")
        with open(program_poll, 'a') as f:
            f.write(f"{poll_results}\n")

    else:
        print('I am sorry you can only choose "yes" or "no".')