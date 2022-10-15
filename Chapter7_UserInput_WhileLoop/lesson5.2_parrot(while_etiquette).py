# Now lets create an additional check so 'quit' not printed when the user types it to end the program.

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    #Here lets add an if statement to check for the work 'quit' before we print anything.
    if message != 'quit':
        print(f"\n{message} ")
