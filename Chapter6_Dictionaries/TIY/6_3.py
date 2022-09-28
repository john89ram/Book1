# Glossary - Dictionaries can be used exactly like normal dictionaries, however they are called glossaries to reduce confusion.
    # Create a glossary of five programming terms you have learned so far in this book.
    # Print each word and its meaning in a neat format. Print the term and in a new line print its meaning. Use the (\n) and (\t) as well.

programming_terms = {
    "variable": "is a place in computer memory with an assigned name.",
    "list": "is a data type that can store a collection of values.",
    "dictionary": "is a data type that stores an unordered collection of data values.",
    "function": "is a reusable block of code that performs a certain action (or actions).",
    "print()": "a function that literally prints the result to the screen.",
    }

print(f"Variable-\n{programming_terms['variable']}.")
print(f"\nList-\n{programming_terms['list']}.")
print(f"\nDictionary-\n{programming_terms['dictionary']}.")
print(f"\nFunction-\n{programming_terms['function']}.")
print(f"\nprint()-\n{programming_terms['print()']}.")
