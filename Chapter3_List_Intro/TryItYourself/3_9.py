#Dinner Guest 
    #Take the end of lab 3.5-6 and use the len() method to find the number of guest that were invited
    
guest_list = ['Bianca','Brooke','Andrew','Lei']

denied_request = 'Bianca'
#Dont forget to save your element as a variable if you plan to remove it and continue to call on it later!!!
guest_list.remove('Bianca')
print(guest_list)

guest_list.insert(0,'Morgan')
guest_list.insert(3,'Nessa')
guest_list.append('Suzi')

print(len(guest_list))