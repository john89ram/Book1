from email import message


first_name = "john"
last_name = "ramirez"

#The "f" before the quotation mark will insert variables vaules to the strings bring used.
full_name = f"{first_name} {last_name}"

#1. Plain print
#print(full_name)

#2. Adding formats to variables
#Here we were able to format the variable inside the print script.
#print(f"Hello, {full_name.title()}!")

#3. Using f-strings to make a message
#message = f"Hello, {full_name.title()}!"
#print(message)

#4. Python3.5 way to format variables
full_name = "{} {}".format(first_name, last_name)
print(full_name)
