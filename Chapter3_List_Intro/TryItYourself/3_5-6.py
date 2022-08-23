#Changing guest list - Some guest are unable to make it to dinner use your skills to make changes to the list
guest_list = ['Bianca','Brooke','Andrew','Lei']
print(guest_list)

denied_request = 'Bianca'
#Dont forget to save your element as a variable if you plan to remove it and continue to call on it later!!!
guest_list.remove('Bianca')
print(guest_list)

guest_list.insert(0,'Morgan')
guest_list.insert(3,'Nessa')
guest_list.append('Suzi')

print(guest_list)

message = f"Hello {guest_list[0].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)
message = f"Hello {guest_list[1].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)
message = f"Hello {guest_list[2].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)
message = f"Hello {guest_list[3].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)
message = f"Hello {guest_list[4].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)
message = f"Hello {guest_list[5].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)

sorry_message = f"{denied_request.title()}, \n\t Sorry you were not able to join us for dinner. \n Sincerely a Millionaire,"
print(sorry_message)