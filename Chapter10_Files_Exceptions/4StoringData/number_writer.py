import os
import json

os.chdir("Chapter10_Files_Exceptions/4StoringData/")

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)