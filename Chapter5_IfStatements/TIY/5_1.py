# Conditional test - Write a series of conditional tests, and print statements describing each
# Examples;
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Now create 10 of your own.
ages = list(range(1,66))

user_age1 = 45
user_age2 = 5

age_pg13 = 13
age_drive = 16
age_consent_tx = 17
age_smoke = 18
age_drink = 21
age_rent_car = 25
age_retire = 65.5

if user_age1 == age_pg13:
    print("Enjoy the movie")
else:
    print("Sorry, try Clifford the big red dog.")

if user_age1 != age_retire:
    print("Get back to work!")

if user_age1 <= age_smoke:
    print("Hey you! Get back to class.")

if user_age1 >= age_drink:
    print("Let's grab a drink.")

if user_age1 > age_rent_car:
    print("Can I see your license?")

if user_age1 < 13:
    print("You are not allowed to ride this ride.")

if (user_age1<age_consent_tx) and (user_age2>age_consent_tx):
    print("Someone call the cops!!!")
   
if (user_age1<age_pg13) or (user_age2>age_consent_tx):
    print("That is cute, is this your kid?")