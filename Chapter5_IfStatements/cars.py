# In this chapter we will learn on if statements and how to use them properly.
    # In this example we have a list of cars, and since car names are proper the need to have a title format
    # BMW needs to be all capitalized but the .title will not cap all the letters for bmw
    # We will use an if statement to find bmw and use .upper instead of .title
cars = ('audi','bmw','subaru','toyota')

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
