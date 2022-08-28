# My pizzas, your pizzas - Use exercise 4.1, make a copy of the list and call it 'friends_pizzas'. Then complete the following task:
    # Add a new pizzas to the original list
    # Add a different pizza to the 'friends_pizzas'
    # Print a message "My favorite pizzas are", use a for loop to print the list. Then print the message "My friend's favorite pizzas are:", and then use a for loop to print the list. 

fav_pizzas = ['pepperoni','meat lovers','supreme']
friends_pizzas = fav_pizzas[:]

fav_pizzas.append('pineapple/ham')
friends_pizzas.insert(0,'jalapeno')

print("My favorite pizzas are:")
for value in fav_pizzas:
    print(value)

print("My friend's favorite pizzas are:")
for value in friends_pizzas:
    print(value)
