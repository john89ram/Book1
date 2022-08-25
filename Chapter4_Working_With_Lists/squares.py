# You can get creative and create any type of number list. Lets create a list of the first 10 squared number from 1-10.
# First lets start with an empty list and put our squares in it.
squares = []
    # Now lets create a for loop with a range.
for value in range(1,11):
        # Now lets create the squares with the numbers in the range.
    #square = value**2
        # Once that is done lets add that square to the list.
    #squares.append(square)
        #----------*** Once you get the how these functions work you can always find a way to simplify.
    squares.append(value**2)
        # ^ This will do the same as lines 7 and 9, once comfortable always try to clean up your code.
# To wrap it up lets print our list with all the squares we created
print(squares)


#----------------------------*** List Comprehensions ***---------------------------------------------


# A more advanced technique when creating a list with numbers are using list comprehensions, which simplify your code to practically one line.
cubes = [value**3 for value in range(1,11)]
# Here this line does the same as the loop before but will cube each number.
print(cubes)
# This can get complicated but once you have a firm understanding can help save a lot of space, and understand other peoples code.

#----------------------------*** Simple Data Collection ***---------------------------------------------

# You can also find simple stats for numbers in your list using the min(), max(), sum() calls
print(min(squares))
print(max(squares))
print(sum(squares))
print(min(cubes))
print(max(cubes))
print(sum(cubes))
