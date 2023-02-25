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
