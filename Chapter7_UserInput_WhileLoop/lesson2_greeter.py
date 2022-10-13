# You should take care when prompting users for inputs.
    # Be sure your instructions are clear and easy to follow, like:

name = input("Please enter your name: ")
print(f"Hello, {name.title()}!")
#-------------------------------------------------------------------------------
# Now we can make this a little more advanced

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your name?"

name = input(prompt)
print(f"\nHello, {name.title()}!")
# This program will set the variable "prompt" as a message and the "+=" will append an additional message to the "prompt" message.
    # Afterwards we will ask the user for input and it will print our "prompt" message
    # We assign the users input to "name" and print a personal message