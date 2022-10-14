# When using the input() function, all input that is entered will be considered a string
    # So when using input() you have to take an extra step to convert the variable to an integer when needing numbers
age = input("How old are you?")
print(age) 
#print(age*age) # <--- Here we can see that this will error out because age is considered a str
#----------------------------------------------------------------------------------------------

# Now lets convert this variable into a int so we can perform mathematical problems with them

age = int(age)
print(age)
print(age*age)
print(age>= 65)
