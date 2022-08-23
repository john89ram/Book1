#-----------------------------------------------Organizing a list
    # sort() method is a simple way to permanently organize your list (alphabetically).

cars = ['bmw','audi','toyota','subaru']
#cars.sort()
#print(cars)

    #You can reverse this order by adding an argument inside the parentheses.
#cars.sort(reverse=True)
#print(cars)

    #If you need to keep the original list but sort it temporarily, use the sort inside of the print command
#print("Here is a sorted list:")
#print(sorted(cars))

#print("Here is the original list:")
#print(cars)

    #To print list in reverse order you can use the reverse() method 
    # *** This will not sort the list in any way!!! Just reverse the order. ***  
cars.reverse()
print(cars)

#-----------------------------------------------Find information on a list
    #len() method can help find the length of a list
print(len(cars))
