# 10-2 Learning C
    # Use the .replace('primary', 'replacement') to replace all instances of Python for C.

filename = 'Chapter10_Files_Exceptions/TIY/10.1.txt'

# Lets read the entire file first

with open(filename) as f:
    contents = f.read()

print(f"\n{contents}")

# Now lets replace Python for C

print(f"\n{contents.replace('Python', 'C')}")
