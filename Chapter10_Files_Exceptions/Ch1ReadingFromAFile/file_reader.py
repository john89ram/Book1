# This only works if both files are in the same directory.

with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)