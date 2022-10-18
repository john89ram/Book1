# Avoiding infinite loops - Simple mistakes can cause infinite loops which inturn can break a program. Be sure you double check your work and test when you are able to.

x = 1
while x <= 5:
    print(x)
    # Just this part of the program will cause an infinite loop since x will never be <= 5 with no additional steps
    x += 1
