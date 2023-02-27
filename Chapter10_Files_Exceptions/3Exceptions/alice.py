### Handling the FileNotFoundError exception ###

#filename = 'Chapter10_Files_Exceptions/3Exceptions/alice.txt' 
#
#with open(filename, encoding='utf-8') as f:
#    contents = f.read()

# same as the Zero error there is no file that python is able to open
    # with open(filename, encoding='utf-8') as f:
    #      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    # FileNotFoundError: [Errno 2] No such file or directory: 'Chapter10_Files_Exceptions
    # 3Exceptions/alice.txt'

# Since the error is with the open() we can place the try block there.

filename = 'Chapter10_Files_Exceptions/3Exceptions/alice.txt' 

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

#---------------------------------------------------------------------------------------------------

### Analyzing text ### 

# Now lets create a program to analyze a txt file. 
# For this project lets simply count how many words within the play "Alice In Wonderland"
# The txt file was copied from: https://www.gutenberg.org/cache/epub/35688/pg35688.txt

alice_txt = "Chapter10_Files_Exceptions/3Exceptions/Alice_In_Wonderland.txt"

try:
    with open(alice_txt, encoding='utf-8') as f_alice:
        content_alice = f_alice.read()
except FileNotFoundError:
    print(f"Sorry, the file {alice_txt} does not exist.")
else:
    # Count the number of words in the file.
    words = content_alice.split()
    num_words = len(words)
    print(f"\n{alice_txt} has about {num_words} words.\n")

#---------------------------------------------------------------------------------------------------

### Working with Multiple Files ### 

# When trying to analyze multiple sources of data it might be easiest to take the bulk of your program and turn it into a function. 

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_object:
            file_contents = f_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the number of words in the file.
        words = file_contents
        num_words = len(words)
        print(f"\n{filename} has about {num_words} words.\n")

# Now we can just call on this function anytime we want to analyze any file.

count_words('Chapter10_Files_Exceptions/3Exceptions/alice.txt')
count_words('Chapter10_Files_Exceptions/3Exceptions/Alice_In_Wonderland.txt')
count_words('Chapter10_Files_Exceptions/3Exceptions/Book_Of_Myths.txt')

#---------------------------------------------------------------------------------------------------

### Failing silently ###

# Sometimes you do not want to see any errors printed during the programming process.
    # If that is the case we can just set the error to "pass" on the error.

def count_words_silentError(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f_object:
            file_contents = f_object.read()
    except FileNotFoundError:
        pass
        # Here when the except block is triggered it is set to pass and nothing further will happen.
    else:
        # Count the number of words in the file.
        words = file_contents
        num_words = len(words)
        print(f"{filename} has about {num_words} words.")

# Lets set our books in a list and run altogether.
filenames = ['Chapter10_Files_Exceptions/3Exceptions/alice.txt',
            'Chapter10_Files_Exceptions/3Exceptions/Alice_In_Wonderland.txt',
            'Chapter10_Files_Exceptions/3Exceptions/Book_Of_Myths.txt']

# For loop to run each file into the function.
for filename in filenames:
    count_words_silentError(filename)
