# Glossary 2 - Take exercise 6_3 and replace all your prints with a loop
    # Add 5 more python terms as well 

programming_terms = {
    "variable": "is a place in computer memory with an assigned name.",
    "list": "is a data type that can store a collection of values.",
    "dictionary": "is a data type that stores an unordered collection of data values.",
    "function": "is a reusable block of code that performs a certain action (or actions).",
    "print()": "a function that literally prints the result to the screen.",
    }

programming_terms['data types'] = "\nInteger (int) = Whole number\nFloat (float) = Decimal number\nString (str) = Text\nBoolean (bool) = True / False\nList (list) = A “container” that can store any kind of values. You can create a list with square brackets e.g. [1, 2, 3, 'a', 'b', 'c'].\nTuple (tuple) = A similar “container” as list with a difference that you cannot update the values in a tuple. You can create a tuple with parentheses (1, 2, 3, 'a', 'b', 'c')."
programming_terms['index'] = 'number is the location of specific value stored in Python lists or tuples. The first index value of list is always 0.'
programming_terms['script '] = 'is a dedicated document for writing Python code that you can execute. Python script files should always have the ".py" file extension.'
programming_terms['repository'] = 'a location where all the files for a particular project are stored, usually abbreviated to "repo." Each project will have its own repo, which is usually located on a server and can be accessed by a unique URL'
programming_terms['commit'] = 'To commit is to write or merge the changes made in the working copy back to the repository. Whe you commit, you are basically taking a "snapshot" of your repository at that point in time, giving you a checkpoint to which you can reevaluate or restore your project to any previous state. The terms "commit" or "checking" can also be used as nouns to describe the new revision that is created as a result of committing.'

for term, explanation in programming_terms.items():
    print(f"\n{term.title()}:{explanation.lower()}")