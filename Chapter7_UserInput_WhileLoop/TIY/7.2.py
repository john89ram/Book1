# Restaurant Seating - Create a program that asks you the number of people are in they're dinner group.
    # Write an if statement that if more then 8 are attending that they will need to wait for a table
    # Otherwise print that there is a table available.

guest_num = input("How many guest will be attending dinner with you today?")
guest_num = int(guest_num)

if guest_num > 8:
    print("Unfortunately we currently do not have a table ready for your party, please wait until we get one set.")
else:
    print("Right this way please.")
