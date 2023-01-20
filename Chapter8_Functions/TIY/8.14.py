# Cars - Create a function that stores information about a car in a dictionary.
    # The function should have the following arguments: Manufacture & Model
    # After which the function and accept any other kind of key-value pairs.

def car_info(make, model, **car_info):
    """ This saves information of a car within a dictionary. """
    car_info["manufacture"] = make
    car_info["model"] = model
    return car_info

car = car_info("Mazda", "3", color = "Red", trim = "Base")

print(car)