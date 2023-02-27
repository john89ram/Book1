# 10-7 Addition Calculator
    # Take what you completed in 10.6 and put it in a while loop so the user can continue.
    

while True:
    print("Please pick two numbers and I will add them together.")
    print("Please enter 'q' at any time to quit.")
    
    num_1 = input("Please enter the first number: ")
    if num_1 == 'q':
        break 
    
    num_2 = input("Please enter the second number: ")
    if num_2 == 'q':
        break
    
    try:
        results = int(num_1)+int(num_2)
    except ValueError:
        print("I am sorry but we can only add numbers.\n")
    else:
        print(f"The answer is {results}.\n")
