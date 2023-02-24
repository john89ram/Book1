
### Reading an Entire File ###

# This only works if both files are in the same directory.
# Can be used path to locate file if Python evnr running in parent directory.
with open('Chapter10_Files_Exceptions/ReadingFromAFile/pi_digits.txt') as file_object:
    contents = file_object.read()

print(f"\n{contents}")
#---------------------------------------------------------------------------------------------------

### File Paths ###

# Script from book but will not run in my evnr.
#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#
#print(contents)

#---------------------------------------------------------------------------------------------------

### Reading line by line ###

# When dealing with absolute paths it is usually best to assign it to a variable.
file_path = 'Chapter10_Files_Exceptions/ReadingFromAFile/pi_digits.txt'
# Here we can print the txt line by line to easily search for data we might need to.

with open(file_path) as file_object:
    for line in file_object:
        print(f"\n{line}")

#---------------------------------------------------------------------------------------------------

### Making a list of lines from a file ###

# Making a list of lines from a file
    # Lets try to use our output that we have made before but outside the func block
with open(file_path) as file_object:
    lines = file_object.readlines()

# We just assigned the readlines output to the "lines" variable.
    # Now we can just print it whenever we might need it.
for line in lines:
    print(line.rstrip())

#---------------------------------------------------------------------------------------------------

### Working with a file's contents ###

