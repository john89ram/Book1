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
# Is this program we set the variable "prompt" as a message and the "+=" will append the following to the "prompt" message.