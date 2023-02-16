# This only works if both files are in the same directory.

# Can be used path to locate file if Python evnr running in parent directory.
with open('Chapter10_Files_Exceptions/Ch1ReadingFromAFile/pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

# Script from book but will not run in my evnr.
#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#
#print(contents)

# When dealing with absolute paths it is usually best to assign it to a variable.
file_path = 'Chapter10_Files_Exceptions/Ch1ReadingFromAFile/pi_digits.txt'
# Here we can print the txt line by line to easily search for data we might need to.

with open(file_path) as file_object:
    for line in file_object:
        print(line)
