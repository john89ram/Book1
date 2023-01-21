# Restaurant - Create a class called Restaurant. The __init__() method should store 2 attributes:
    # restaurant_name & cuisine_type
    # create a method called describe_restaurant() that prints the attributes above.
    # lastly create a method named open_restaurant that prints a message that the store is open.

class Restaurant:
    """ A simple class to create a restaurant and accepting the attributes name and cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes of the restaurant"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Simple return of the attributes of the restaurant."""
        print(f"Welcome to the {self.name}! We serve {self.cuisine} food.")

    def open_restaurant(self):
        """Simple message to indicate that a restaurant is open"""
        print(f"The {self.name} is now open!")

taco_shop = Restaurant("Silly Chilly", "Mexican food")

print(taco_shop.name)
print(taco_shop.cuisine)

taco_shop.describe_restaurant()
taco_shop.open_restaurant()