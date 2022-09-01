#  Create a new list and make a couple of conditional test
    # Test for == and !=
    # Test using the lower() method
    # Test wether an item is or is not in the list 

techs_in_office = ['tim','luke','jacob','sam','jack','greg']

print("Is Tim in the office today?")
print('tim' in techs_in_office)

sick_employees = techs_in_office.pop()

print(sick_employees=='Greg'.lower())
print(sick_employees!='tim')
print('Greg'.lower() in techs_in_office)
print('Tim'.lower() in techs_in_office)
