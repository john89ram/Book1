# The "=" will assign the variable 
# The "==" ask wether or not the variable is "equal to" the if statement. (returning true or false)
# You can also "!=" this means "not equal to. For example"
requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print('Hold the anchovies!')

# You can also request if an element is "in" a list

requested_toppings = ['mushrooms','onions','pineapple']

# In the Python environment you can call "'mushrooms' in requested_toppings" and Python will return "True"

#------------------------------------------*** Testing conditions cont. *****************************************
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your 1st pizza\n")
# This is testing for exact conditions when creating this users pizza.
#-
# This code will not work like the last one and will stop once the first statement calls back True
requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your 2nd pizza\n")

#------------------------------------------*** Checking for special items *****************************************

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your 3rd pizza!\n")
#------------------------------------------*** Checking for special items (Ran out of an item in the list) *****************************************

requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your 4th pizza!\n")
#------------------------------------------*** Checking that a list is not empty *****************************************

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your 5th pizza!")
else:
    print("Are you sure you want a plain pizza?")
# Here this code uses the for loop to check for all requested toppings inside the list (which has nothing)
    # This triggers the else block and returns the plain pizza message.

#------------------------------------------*** Working with multiple list *****************************************

available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your 6th pizza!")
# In this example we start a for loop to cycle through all the requested toppings and compare them to the available toppings.
    # If they are found inside the available list, then they are added to the pizza
    # If they are not found in the list, then the else block is triggered and the Sorry message is printed