#Practicing to modify list add/delete/change 
motorcycles = ['honda','yamaha','suzuki']
#print(motorcycles)

#Modifying an element to a list
#motorcycles[0] = 'ducati'
#print(motorcycles)

#Appending will add to an element to the end of the list.
#motorcycles.append('honda')
#print(motorcycles)

#--------------------------------------------- Using own examples -------------------------------------------------------------------------------------

#You can so start with an empty list and append items as the program continues.
fav_foods = []
#print(fav_foods)

fav_foods.append('burger')
fav_foods.append('pizza')
fav_foods.append('pasta')
#print(fav_foods)

#Inserting elements into a list. Inserting an element will shift all others to the right of the index placement.
fav_foods.insert(1, 'TACOS')
#print(fav_foods)

#Removing elements by index, you must know the position of the element in order to delete by this method.
    #Elements that are deleted can not be accessed afterwards
del fav_foods[1]
#print(fav_foods)

#When wanting to continue to access elements that are removed from a list you can use the pop method instead of del
    #This will remove the element from the list but still have the ability to access it.
    #By default the pop method will take from the end of the list (hence the "POP"- like Mentos the fresh maker)
popped_fav_foods = fav_foods.pop()
#print(fav_foods)
#print(popped_fav_foods)

#You can use the pop value as a normal variable like any other,
    #For instance if you listed your favorite foods by most to least favorite you can pop them and use them in a message
#print(f"Out of all my favorite foods, {popped_fav_foods.lower()} are the ones I like the least.")

#----------------------------------------- Using new examples ----------------------------------------------------------------------------

#Popping from index in a list
    # *** Remember when the element has been popped it can no longer be accessed within the list
contigo_techs = ['Tim', 'Luke', 'Jacob', 'Sam', 'Jack', 'Greg']
print(contigo_techs)

tech_2 = contigo_techs.pop(4)
#print(contigo_techs)
#print(tech_2)

#print(f"{tech_2.title()} is our current Tech 2 and as such able to do On-site visits.")
#print(contigo_techs[5])

#Elements can also be removed by their value, this is useful if you do not know the index. 
contigo_techs.remove('Tim')
print(contigo_techs)

    #You can also assign the element a variable and call on the variable when removing as well.
contigo_techs.append('Tim')
print(contigo_techs)

most_feared_tech = 'Tim'
contigo_techs.remove(most_feared_tech)

print(f"No one messes with {most_feared_tech.title()} in the office, for fear of being destroyed.")
print(contigo_techs)
