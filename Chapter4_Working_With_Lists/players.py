# Slicing a list - In this section we will learning how to manipulate a list with strings.
players = ['charles','martina','michael','florence','eli']
# Now lets call the first 3 players in the list (do not forget the off-by-one rule)
print(players[0:3])
# Now lets call the 2nd - 4th players
print(players[1:4])
# If you omit the first input in the bracket it will start at the beginning of the list
print(players[:4])
# Same is true if you omit the last argument
print(players[2:])
# Remember that you can also use negative numbers as arguments as well (which will count backwards starting with the end of the list)
print(players[-3:])