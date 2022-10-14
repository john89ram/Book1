# Using the modulo operator '%' - The '%' will divide a number by another number but will only return the remainder. 
    #(ex. 4/5 = 1 with a remainder of 1 so '%' will output 1)
    # Lets use this to see of an operation is even or odd.

number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"The number {number} is odd.")