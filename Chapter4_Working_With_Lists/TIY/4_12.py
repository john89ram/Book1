my_foods = ['chick-fil-a','mexican food','pizza']
friends_foods = my_foods[:]

my_foods.append('risotto')
friends_foods.append('chicken nuggies')

print('My favorite foods are:')
for value in my_foods:
    print(value)
print('\nMy friends favorite foods are:')
for value in friends_foods:
    print(value)