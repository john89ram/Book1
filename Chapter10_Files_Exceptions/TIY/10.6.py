# 10-6 Addition
    # Create a program that request the user to add two numbers together, and prints the results.
    # Create a try block to prevent a ValueError when trying to add anything that is not an int.
        # and print a friendly error message.
    # Test your program by entering two integers as well as a int and a string and 2 strings.

print("Please pick two numbers and I will add them together.")
num_1 = input("Please enter the first number: ")
num_2 = input("Please enter the second number: ")

try:
    results = int(num_1)+int(num_2)
except ValueError:
    print("I am sorry but we can only add numbers.")
else:
    print(f"The answer is {results}.")
