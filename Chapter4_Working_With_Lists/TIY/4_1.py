# Make a list of 3 of your favorite pizzas, then write a for loop to print the names of your list.
    # Mod your for loop to print a sentence with your pizza 
    # Add a closing statement outside of the for loop

fav_pizzas = ['pepperoni','meat lovers','supreme']

print('I love all types of pizza, so much. But I have a couple of faves, and they are.\n')

for fav_pizza in fav_pizzas:
    #print(fav_pizza)

    message = f"{fav_pizza.title()} is AMAZING!"
    print(message)

print('\nBut honestly who can just choose a couple of pizzas? \nI know you may think I am crazy but...\n\tSeriously *whisper* I think pineapple and ham pizza is great as well.')