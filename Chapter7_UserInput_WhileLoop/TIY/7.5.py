# Movie tickets - A movie theater charges different ticket prices depending on the age. 
    # The prices are < 3 are free, 3 - 12 are $10, and > 12 are $15
    # Write a loop which ask the users age and then tell them the total cost

num_users = int(input("Hello! Welcome to the movie theater."
    "\nHow many people will be joining you today? "))

current_count = 0
total_cost = 0

while current_count < num_users:
    age = int(input("How old is this person? "))
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    elif age > 12:
        total_cost += 15
    
    current_count += 1

print(f"Your total cost is ${total_cost}.")
