# 10-1 Learning python:
    # Create a txt file and write a couple of things you learned about python so far.
    # Write a program that reads the file and prints what you wrote 3 times
        # Print once by reading the entire file
        # Another by looping over the file object
        # And lastly by storing the lines in a list and then working with them outside
            # the with block

# Set the txt file as a variable to easily interact with it
filename = 'Chapter10_Files_Exceptions/TIY/10.1.txt'


# Read the entire file contents (Reading an entire file)
print(f"\nReading the entire file content: ")
with open(filename) as f:
    contents = f.read()

print(contents)

# Looping over the lines (Reading line by line)
print(f"\nLooping over lines: ")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

# Storing lines in a list (Making a list of lines from a file)
print(f"\nStoring the lines in a list: ")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())