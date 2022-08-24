# Make a list of 5 places in the world you would like to visit
    #1. Do not organize the list / Print the original form of the list
    #2. Temporarily sort the list / Print / Print original list to show the list was not affected
    #3. Temporarily sort in reverse order / Print / Print original list to show the list was not affected
    #4. Use the reverse method on the list / Print
    #5. Use the reverse method once again on the list / Print
    #6. Sort the list with the sort() method / Print
    #7. Sort the list in reverse with the sort() method / Print 

places2visit = ['singapore','japan','france','new york','england']
#1
print(places2visit)
#2
print(sorted(places2visit))
print(places2visit)
#3
print(sorted(places2visit, reverse=True))
#4
places2visit.reverse()
print(places2visit)
#5
places2visit.reverse()
print(places2visit)
#6
places2visit.sort()
print(places2visit)
#7
places2visit.sort(reverse=True)
print(places2visit)