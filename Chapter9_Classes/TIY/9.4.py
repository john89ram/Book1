# Number Served - Copy TIY 9.1, and an attribute called number_served
    # Set the default value to number_served to 0
    # Create an instance called "restaurant" from this class. 
    # Print the number of customers the restaurant has served, then change the value and print again
        # Now lets add a method called set_number_served() that lets you set the number of customers
            # that have been served. Call this method with a new number and print
        # Lastly add another method called increment_number_served() that lets you increment the 
            # number of customers who have been served. Call this method with any number that would 
            # represent the number of customer served within a business day.

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
