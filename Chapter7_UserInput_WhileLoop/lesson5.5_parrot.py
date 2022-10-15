# Lets like lesson 1 we are going to implement what we just learned
    # Instead of the program ending after the input from the user create a while loop
    # to stop when the user types "quit"

prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

message = ""

while message != 'quit':
    message = input(prompt)
    print(f"\n{message}")
