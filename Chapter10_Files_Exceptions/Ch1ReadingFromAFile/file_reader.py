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