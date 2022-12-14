#List - A collection of items in a particular order.
#    In Python list use the "[]" brackets to hold objects.

bicycles = ['trek','cannondale','redline','specialized']

#Printing the list itself will print the entire list including the brackets
#print(bicycles)

#You can also call an item in the list by referencing the index (numbered position in the list)
#['trek','cannondale','redline','specialized'] = ['0','1','2','3'] <- Index position
#print(bicycles[0])

#You can also use the format from Ch.2 tools to make outputs professional for the end-user.
#print(bicycles[1].title())
#print(bicycles[3].title())

#When a list gets large to call easily you can make the call with negative numbers.
#print(bicycles[-1])

#Creating a message using a list and calling values.
message = f"My first bike was a {bicycles[3].title()} bicycle."
print(message)
