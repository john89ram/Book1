# We will take a look on how tuples work.
    # Tuples function a lot like list, however they are unchanging. 
    
# We are going to set dimensions for a rectangle in a tuple to ensure that the measurements never change.
dimensions = (200,50)
    # Tuples are created with "( )" instead of the "[ ]". 
print(dimensions[0])
print(dimensions[1])
    # When calling elements within a tuple you can by using the index number like a list.

# Now lets try to make a change to the dimensions. 
#dimensions[0] = 250
#print(dimensions[0])
    # We get an error code, because we can not make changes to a tuple 
   
# To make changes to a tuple you will need to reassign the variable.
dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)