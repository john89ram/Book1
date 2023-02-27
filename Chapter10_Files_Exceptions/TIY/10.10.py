# 10-10 Common words 
    # Pick one of the text files and analyze the file to count the number of "the" is in the file.
    # Use the count() method during your analysis the first time
    # Afterwards use count but place a space after the searched word 'the ' record the results
    # Lastly wrap this search in a .lower() and record the results

import os

os.chdir("Chapter10_Files_Exceptions/3Exceptions/")

def word_count(filename, word):
    """This program will search for a desired word within a chosen text file"""
    try:
        with open(filename, encoding='utf-8') as f_object:
            f_contents = f_object.read()
    except FileNotFoundError:
        print(f"Sorry, not able to find the {filename} file.")
    else:
        #count = f_contents.count(word)
        count = f_contents.lower().count(word)
        print(f"Inside the file {filename}, the word {word} was counted {count} times.")
        
word_count('Alice_In_Wonderland.txt', 'the ')