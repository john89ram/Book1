
### Reading an Entire File ###

# This only works if both files are in the same directory.
# Can be used path to locate file if Python evnr running in parent directory.
with open('Chapter10_Files_Exceptions/1ReadingFromAFile/pi_digits.txt') as file_object:
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
file_path = 'Chapter10_Files_Exceptions/1ReadingFromAFile/pi_digits.txt'
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
    # Now we can just print it whenever we might need it (saving the txt file into memory).
for line in lines:
    print(f"\n{line.rstrip()}")

#---------------------------------------------------------------------------------------------------

### Working with a file's contents ###

# Now lets work with the txt file now that it is saved into memory. 
    # Lets put it into a single line with no breaks

pi_string = ''
# Here we set pi_string as an empty variable, this is a place holder so we can transfer the data in
    # lines (pi_digits.txt) into pi_string
for line in lines:
    pi_string += line.rstrip()
    # Now with each line we are stripping the '\n' that readlines() hides while operating
        # giving us just the tabs only that we created formatting the txt file 
print(pi_string)
print(len(pi_string))

# Lets continue by just using the strip() method and get rid of all whitespace
    # Lets use another place holder called pi_string2
        # We can still use the lines variable bc we did not alter the data, hence the empty variable
pi_string2 = ''

for line in lines:
    pi_string2 += line.strip()

print(pi_string2)
print(len(pi_string2))
# Now there is no space and pi is back together, we have len() to confirm this as well

#---------------------------------------------------------------------------------------------------

### Large files: One million digits ###

filename = 'Chapter10_Files_Exceptions/1ReadingFromAFile/pi_million_digits.txt'

with open(filename) as file_object:
    mil_lines = file_object.readlines()

pi_string_mil = ''

for mil_line in mil_lines:
    pi_string_mil += mil_line.strip()

print(f"{pi_string_mil[:52]}...")
print(len(pi_string_mil))

#---------------------------------------------------------------------------------------------------

### Is your birthday contained in pi ###

# Now lets play with the data and see if we can create a script to search for a birthday in pi

# Simple user input requesting 6 digits and assigning them to "birthday"
birthday = input(f"\nEnter your birthday, in the form mmddyy: ")

# Now an easy if statement to see if the 6 character string is anywhere in the pi_million txt file
if birthday in pi_string_mil:
    print(f"Your birthday appears in the first million digits of pi!")
else:
    print(f"You birthday does not appear in the first million digits of pi.")