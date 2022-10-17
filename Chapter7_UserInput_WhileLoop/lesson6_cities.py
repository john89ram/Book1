# There are other ways to end a program other then what we have learned
    # Another option is to use the "break" statement - this will abruptly end the program

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\nEnter 'quit' to end the program. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")
