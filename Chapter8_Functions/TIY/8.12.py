# Sandwiches - write a function that accepts a list of items a person wants on a sandwich.
    # You should have 1 parameter that can accept as many items as needed, and print the sandwich.
    # Then create 3 different types of sandwiches. 

def build_sandwich(name, bread_type, *toppings, **sandwich_order):
    """ This is a function to take a sandwich order of a user """
    sandwich_order['order_name'] = name
    sandwich_order['order_bread'] = bread_type
    sandwich_order['order_toppings'] = toppings
    return sandwich_order

sandwich1 = build_sandwich("John", "Brown bread", "egg salad", "mojo criollo", "nuts", "butter lettuce", special_request = "pinch of kosher salt")

print(f"{sandwich1}\n")

sandwich2 = build_sandwich("Ashley", "Wonder bread", "champagne vinegar", "radish slices","sea salt", bean_switch = "black beans", cheese_switch = "Havarti cheese",sandwich_addition = "dried cranberries")

print(f"{sandwich2}\n")

sandwich3 = build_sandwich("Michael", " Hawaiian roll", "carne asada", "cream cheese", sandwich_addition1 = "greek yogurt", sandwich_addition2 = "fried noodles", sandwich_addition3 = "parsley")

print(f"{sandwich3}\n")