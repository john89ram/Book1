#Your dinner table is not ready anymore and you can only have 2 guest.
    #Create a message "From" the restaurant to inform you that you can only receive 2 guest
    #Use the pop method to remove your guest one by one and send them a message that they will not be able to attend.
    #Print a message to the final 2 people who are invited to dinner.
    #When complete del the last users from the list and print the list
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

popped_guest= guest_list.pop()
sorry_message = f"{popped_guest.title()}, \n\t Sorry you were not able to join us for dinner. \n\n Sincerely a Millionaire,"
print(sorry_message)

popped_guest= guest_list.pop()
sorry_message = f"{popped_guest.title()}, \n\t Sorry you were not able to join us for dinner. \n\n Sincerely a Millionaire,"
print(sorry_message)

popped_guest= guest_list.pop()
sorry_message = f"{popped_guest.title()}, \n\t Sorry you were not able to join us for dinner. \n\n Sincerely a Millionaire,"
print(sorry_message)

popped_guest= guest_list.pop()
sorry_message = f"{popped_guest.title()}, \n\t Sorry you were not able to join us for dinner. \n\n Sincerely a Millionaire,"
print(sorry_message)

message = f"Hello {guest_list[0].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)
del guest_list[0]
message = f"Hello {guest_list[0].title()},\n\n\t You are invited to join me for dinner and drinks to celebrate my first million dollars. \n\n\t Thank you,"
print(message)
del guest_list[0]

print(guest_list)