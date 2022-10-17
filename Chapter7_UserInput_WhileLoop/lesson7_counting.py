# Now instead of a "break" statement you can use the "continue" statement
    # This will act like a gate and if the program returns true the gate will open.
    # Let see how this works with a simple counting program. 

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)