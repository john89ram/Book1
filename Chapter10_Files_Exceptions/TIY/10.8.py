# 10-8 Cats and Dogs
    # Make two files "cats.txt" and "dog.txt"
    # Store 3 names of each of the animal files
    # Write a a program that reads these files and print its contents
    # Then wrap your code in a try-except black to catch the FileNotFound error
        # and print a message that the file is not there
        # Move one of the files to a different location to test the script
        
import os

os.chdir("Chapter10_Files_Exceptions/TIY/")

cat_file = '10.8_cats.txt'
dog_file = '10.8_dogs.txt'


try:
    with open(cat_file) as c_object:
        cat_names = c_object.read()
except FileNotFoundError:
    print(f"I am sorry but I do not see {cat_file} in this directory.")
else:
    print(cat_names)

try:    
    with open(dog_file) as d_object:
        dog_names = d_object.read()
except FileNotFoundError:
    print(f"I am sorry but I do not see {dog_file} in this directory.")
else:
    print(dog_names)