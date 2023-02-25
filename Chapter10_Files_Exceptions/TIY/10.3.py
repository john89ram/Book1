# 10-3 Guest:
    # Write a program that prompts the user for their name. 
    # When they respond, write their name to a file called guest.txt

guest = input("Hello! What name should I save in our system? ")
file_path = "Chapter10_Files_Exceptions/TIY/10.3.txt"

with open(file_path, 'w') as f:
    f.write(guest)

with open(file_path, 'r') as f:
    confirmation = f.read()

print(f"Thank you {confirmation}. We have saved your name!")