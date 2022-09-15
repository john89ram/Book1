# Ordinal Numbers - Ordinal numbers indicate their position in a list; such as 1st, or 2nd. Most Ordinal Numbers end in "th", expect for 1, 2, and 3.
    # Store the numbers 1 - 9 in a list
    # Loop through the list.
    # Use an if-elif-else chain to print the proper ordinal number ending for each number. (1st, 2nd, 3rd, 4th, etc.)
    # Be sure each number prints on its own line.

ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f"{ordinal_number}"+"st")
    elif ordinal_number == 2:
        print(f"{ordinal_number}"+"nd")
    elif ordinal_number == 3:
        print(f"{ordinal_number}"+"rd")
    else:
        print(f"{ordinal_number}"+"th")