### Handling the ZeroDivisionError exception ###

# As you know it is not possible to divide by 0, and Python will show the same.

#print(5/0)
    # when you try this error will show up
    # print(5/0)
    #       ~^~
    # ZeroDivisionError: division by zero

# These errors can crash the whole program and sometimes we need to get around them. 

#---------------------------------------------------------------------------------------------------

### Using try-except Blocks ###

# When there might be an error issue you can use a try-except block to get around it and still 
    # show issues that might occur.

try:
    print(5/0)
except ZeroDivisionError:
    print("You can not divide by zero!")
# Now we see that even though we got an error the program was able to complete itself.

#---------------------------------------------------------------------------------------------------

### Using exceptions to prevent crashes ###

print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

#while True:
#    first_num = input(f"\nFirst number: ")
#    if first_num == 'q':
#        break
#    
#    second_num = input(f"\nSecond number: ")
#    if second_num == 'q':
#        break
#
#    answer = int(first_num)/int(second_num)
#    print(answer)

# Here we can see that we run into the same issue as the first which is a "ZeroDivisionError"
    # The error cause the program to crash, so lets take what we learned and make an exception.

#---------------------------------------------------------------------------------------------------

### The else Block ###
while True:
    first_num = input(f"\nFirst number: ")
    if first_num == 'q':
        break

    second_num = input(f"\nSecond number: ")
    if second_num == 'q':
        break

    # Here we can enter the try block to prevent any errors occurring and will print the answer
        # and not crash the program.
    try:
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print("You can not divide by zero!")
    else:    
        print(answer)

#---------------------------------------------------------------------------------------------------

