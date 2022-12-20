# Modifying a list in a function - You can modify list with functions as well.
    # Lets take a simple list, that will simulate printing each design, until none are left.
    # Here we are going to create a script to that can do that without a function.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Here we have our 2 lists. One that needs to be processed and the other when the model has been printed

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print(f"\nThe following models have been printed:")
for completed_models in completed_models:
    print(completed_models)