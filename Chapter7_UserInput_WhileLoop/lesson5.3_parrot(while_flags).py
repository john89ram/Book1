# There are times when we need to end a program for a multitude of other checks. (no more lives in a game, or time runs out, etc.)
    # We can create flags to check for constant conditions, and when triggered to flip the flag and end the program.
    # Lets create a simple one in the parrot program.

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(f"{message}")
