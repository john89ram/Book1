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

print("\nFinished making your pizza")
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

print("\nFinished making your pizza")
