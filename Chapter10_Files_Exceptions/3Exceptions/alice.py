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
