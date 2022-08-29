# "!=" and "==" can also be used with numbers
answer = 17

if answer != 42:
    print('That is not the correct answer. Please try again!')

# When using integers you can also use ">",">=","<", and "<="

your_age = 18
friends_age = 17

if your_age >= 21:
    print("Let's grab a drink!")
else:
    print("Sorry too young my friend")

# You can also set up an "and" condition as well as an "or" condition
    # "And" - condition means that all inquiring must return true for the next block to trigger
    # "Or" - condition means that at least one condition must return true to trigger

bar_age = 21
club_age =18

if your_age and friends_age >= bar_age:
    print("Cheers mate!")
else:
    print("Sorry friends you are too young.")

# Using the () can help when troubleshooting your code
if (your_age >= club_age) or (friends_age >=club_age):
    print("Let's dance!")
else:
    print("I guess we're going to Chuck E Cheeses...")