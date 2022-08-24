#Every function - Create your own custom list while doing so use everything you learned in this chapter at least once.
    # Create list, use methods like; .append(), .insert(), del, .pop(), .remove()
    # Print list
    # Sort the list with all organizing methods in this chapter; .sort(), .sort(reverse=True), print(sorted(listexp)), print(sorted(listexp,reverse=True)), .reverse(), len(listexp)
    # Access an element within list; print(listexp[])
    # Use the index within list to create a message

#---------------*** Capitalization will interfere when sorting a list on Python ***

contigo_employees = ['bryan','marc','andrew','stephanie','renee','preston','joel','jonathan','greg','jack','luke','tim','tegan','blas','grant','varon','izzy','chris','nathan','kyle','colton','jarod','JD','nick','micah','anthony','monty','mason','stella']
print(len(contigo_employees))
print(contigo_employees)

#Removing employees that longer active
popped_employee = contigo_employees.pop()
print(contigo_employees)
print(popped_employee)

del contigo_employees[27]
print(contigo_employees)

contigo_employees.remove('stephanie')
print(contigo_employees)

#Adding new employees to the list
contigo_employees.append('sam')
print(contigo_employees)

contigo_employees.insert(7,'jacob')
print(contigo_employees)

#Sort the list impermanently 
print(sorted(contigo_employees))
print(sorted(contigo_employees,reverse=True))

contigo_employees.reverse()
print(contigo_employees)
contigo_employees.reverse()
print(contigo_employees)

#Sort the list permanently
contigo_employees.sort()
print(contigo_employees)

contigo_employees.sort(reverse=True)
print(contigo_employees)

message = f"Contigo is a small MSP firm with great guys to help you out in any situation, and the leader of this mighty group is {contigo_employees[23].title()}!"
print(message)