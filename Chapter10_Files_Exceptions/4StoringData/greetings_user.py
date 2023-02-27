import os
import json

os.chdir("Chapter10_Files_Exceptions/4StoringData/")
filename = 'username.json'

#---------------------------------------------------------------------------------------------------

### Saving and reading User-generated data (Part 2) ###
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
