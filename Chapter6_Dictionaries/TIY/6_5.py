# Rivers - Create a dictionary containing three major rivers and the country they belong to
    # Use a loop to create a sentence about each river (ex. The Nile runs through Egypt.)
    # Use a loop to print the name of each river
    # Use a loop to print the name of each country

major_rivers = {'The Amazon River': 'Ecuador, Colombia, Venezuela, Bolivia, and Brazil','The Nile River': 'Burundi, Tanzania, Rwanda, the Democratic Republic of the Congo, Kenya, Uganda, Sudan, Ethiopia, and South Sudan','The Mekong River': 'China, Myanmar, Thailand, Lao PDR, Cambodia and Viet Nam'}

for river ,countries in major_rivers.items():
    print(f"\n{river.title()}, travels through {countries.title()}. Isn't that AMAZING!")

print(major_rivers.keys())
print(major_rivers.values())