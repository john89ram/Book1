# Were going to write an if-elif-else chain over a person's stage in life
    # Set a variable to to determine a persons age and then,
    # Test if a person is less then 2 years old, and print that the person is a baby.
    # Or if they are at least 2 years old but less then 4, print that person is a toddler
    # Or if they are at least 4 years old but less then 13, print that person is a kid
    # Or if they are at least 13 years old but less then 20, print that person is a teenager
    # Or if they are at least 20 years old but less then 65, print that person is a adult
    # Or if they are at least 65 years old, print that person is a elder

user_age = 21

if user_age<2:
    print("You are a baby.")
elif user_age>=2 and user_age<=4:
    print("You are a toddler.")
elif user_age>=4 and user_age<=13:
    print("You are a kid.")
elif user_age>=13 and user_age<=20:
    print("You are a teenager.")
elif user_age>=20 and user_age<=65:
    print("You are a adult.")
else:
    print("You are an elder.")