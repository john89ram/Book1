# Here we use the "**" to create an empty dictionary to accept any name-value pairs.
    # This is helpful when we are unsure to the amount of data that will be entered.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
# Here after the names parameters "first/last_names", the user added location and field.
    # Similar to this example all that is needed is the parameter and the data linked to it.
                            location = "princeton",
                            field = "physics")

print(user_profile)    