### Writing to an empty file ###

# Dont forget that the file location can be designated when creating the variable.
    # If no file path is called then it will be created in the working directory.
filename = 'Chapter10_Files_Exceptions/2WritingToAFile/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming!")

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

#---------------------------------------------------------------------------------------------------

### Writing multiple lines ###

# Be aware that when using the write function that Python will erase and write over a file if it 
    # already has data on it.

with open(filename, 'w') as f:
    f.write("I love programming!\n")
    f.write("I love creating new games.\n")

with open(filename) as f:
    rewrite = f.read()

print(rewrite)

#---------------------------------------------------------------------------------------------------

### Appending to a file ###

# Somethings you do not want to erase everything and write it all over again. 
# So instead lets open the file in append mode so anything we write just gets added on the end

with open(filename, 'a') as f:
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I love creating apps that can run in a browser.\n")

with open(filename) as f:
    rewrite = f.read()

print(rewrite)

# By default open() will be set to read ONLY but other modes can be selected
    # 'r' read mode - if you want to call it
    # 'w' write mode - write on top of any saved data (also create the file if not created already)
    # 'a' append mode - add to the end of the data (also create the file if not created already)
    # 'r+' read and write mode - has both characteristic of 'r' and 'w' 
        # mainly used while working within the with block. 

