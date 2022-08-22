#Practicing to modify list add/delete/change 
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#Modifying an element to a list
motorcycles[0] = 'ducati'
print(motorcycles)

#Appending will add to an element to the end of the list.
motorcycles.append('honda')
print(motorcycles)

#You can so start with an empty list and append items as the program continues.
fav_foods = []
print(fav_foods)

fav_foods.append('burger')
fav_foods.append('pizza')
fav_foods.append('pasta')
print(fav_foods)

#Inserting elements into a list. Inserting an element will shift all others to the right of the index placement.
fav_foods.insert(1, 'TACOS')
print(fav_foods)

#Removing elements by index, you must know the position of the element in order to delete by this method.
    #Elements that are deleted can not be accessed afterwards
del fav_foods[1]
print(fav_foods)

