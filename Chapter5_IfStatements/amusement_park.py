# Now were going to make a if-elif-else chain (a more complex if statement)
    # Lets make an if-elif-else chain for price of admission to a park
    # Under the age of 4 are free
    # Ages between 4 and 18 cost $25
    # Ages 18 and older are $40

age = 65

if age<4:
    print("Your child is free please enjoy the park.")
elif age<18:
    print("That will be $25 please.")
else:
    print("$40 please.")

print("Please enjoy the park!")

# We can shorten this to make the set price as a variable and have it call that variable at the end.

if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
else:
    price=20

print(f"The cost of admission will be ${price} please.")

# You can also have all elif blocks when you need the code to be precise.

if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
    price=20

print(f"The cost of admission will be ${price} please.")
# With this change the code must fulfil one of these requirements to execute any code, where the "else" statement will execute if the others fail.