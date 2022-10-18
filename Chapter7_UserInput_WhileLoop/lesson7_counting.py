# Now instead of a "break" statement you can use the "continue" statement
    # This will act like a gate and if the program returns true the gate will open.
    # Let see how this works with a simple counting program. 

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
# In this program we set the "current_number" to 0, and create a while loop to stay open until the number hits 10
    # then it will continue to add 1 to the current number. (this is basics)
    # but afterwards we created an if statement to divide the current number by 2 (with no returns) and if that is true the program will "continue"
    # this will reset the program back to the top of the loop, if false it will print the current number (which should print all odd numbers).