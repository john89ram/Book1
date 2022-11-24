# We are going to use the same code as we did in the beginning of this lesson.
    # We will create 2 functions one to handle the printing and the other
    # to display the completed message.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """
    Show all the models that were printed.
    """
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function from modifying a list - If you need to save the original list 
    # you can always make a copy by using '[:]' when calling the list in the function.
    # Lets says we want to keep the unprinted_design list for records. Well with our current
    # setup we are the .pop will leave our list empty.

print(f"\n{unprinted_designs}")

# Lets try to use a copy of our list instead of the list itself.

unprinted_designs = ['boat test', 'pikachu', 'cube']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
