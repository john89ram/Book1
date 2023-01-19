# User Profiles - Start with a copy of user_profile from lesson9. 
    # Build a profile yourself by calling build_profile(), and create a profile
    # with 3 additional attributes.

# Here we use the "**" (aka "kwargs" - keyword arguments) to create an empty dictionary.
    # This is helpful when we are unsure to the amount of data that will be entered.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile("Jonathan", "Ramirez", 
                                birthday = "Oct 25, 1989",
                                married_status = "Married",
                                number_children = 2)

print(user_profile)    