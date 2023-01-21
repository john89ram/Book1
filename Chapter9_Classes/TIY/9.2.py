# Use the code from 9.1 and create 3 different restaurants with your class.

class Restaurant:
    """ A simple class to create a restaurant and accepting the attributes name and cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes of the restaurant"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Simple return of the attributes of the restaurant."""
        print(f"Welcome to the {self.name}! We serve {self.cuisine}.")

    def open_restaurant(self):
        """Simple message to indicate that a restaurant is open"""
        print(f"The {self.name} is now open!")


restaurant_1 = Restaurant("Dale's Essenhaus", "American food")
restaurant_2 = Restaurant("Pizza Hut", "Fast food")
restaurant_3 = Restaurant("T-Loc's Sonora Hot Dogs", "Mixed")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
