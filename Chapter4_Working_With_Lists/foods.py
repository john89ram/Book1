# Copying a list can be a useful tool to have that can save some time.
my_foods = ['chick-fil-a','mexican food','pizza']
    # Since there is no arguments that are placed in the brackets it will copy the entire list
friends_foods = my_foods[:]

#------------------------- Adding to the list ------------------------------------------------------
    #To make changes to the list separately they need to be added after the initial copy
my_foods.append('risotto')
friends_foods.append('chicken nuggies')

print('My favorite foods are:')
print(my_foods)

print('\nMy friends favorite foods are:')
print(friends_foods)

