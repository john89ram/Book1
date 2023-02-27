import os
import json

os.chdir("Chapter10_Files_Exceptions/4StoringData/")

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)