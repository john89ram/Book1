# In this chapter we are going to work with list, and use more advanced operations
    # For loops help simplify task while working down a list.
magicians = ['alice','david','carolina']
for magician in magicians:
#   print(magician)
    print(f"{magician.title()}, that was a great trick!")
#-----------------------------*** Playing with different ways to print ***
    #message = f"{magician.title()}, that was a great trick!"
    #print(message)
#-----------------------------*** Back to your scheduled programming ***
    print(f"I can't wait to see your next trick, {magician.title()}!\n")

    #Now it is time to create a message at the end of the loop and continue on.
print(f"Thank you, everyone. That was a great magic show!")

