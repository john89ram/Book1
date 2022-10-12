# Buffet - A restaurant offers the exact same 5 dishes, create a tuple to store these dishes.
    # Create a for loop to print each meal
    # Try to modify one of these items, and make sure Python rejects these changes
    # The restaurant finally made changes to the menu and will replace 2 dishes. Create a message advertising the changes.

buffet_dishes = ('bbq pork','marry me chicken','cobb salad','taco salad','stuffed peppers')

print("Hello, and welcome to Buffet 'ole!\nPlease take a look at our menu this season.")
for value in buffet_dishes:
    print(value)
    
#buffet_dishes.remove('stuffed peppers')

buffet_dishes = ('bbq pork','marry me chicken','cobb salad','soup of the day','fajitas')
print("Try our new surpirse menu; (limited time only)")
for value in buffet_dishes:
    print(value)