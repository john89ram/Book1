# 10-9 Silent cats and dogs
    # Modify your script in 10.8 to fail silently instead of the message.

import os

os.chdir("Chapter10_Files_Exceptions/TIY/")

cat_file = '10.8_cats.txt'
dog_file = '10.8_dogs.txt'


try:
    with open(cat_file) as c_object:
        cat_names = c_object.read()
except FileNotFoundError:
    pass
else:
    print(cat_names)

try:    
    with open(dog_file) as d_object:
        dog_names = d_object.read()
except FileNotFoundError:
    pass
else:
    print(dog_names)