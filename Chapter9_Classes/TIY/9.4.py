# Number Served - Copy TIY 9.1, and create an attribute called number_served
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
        # New attribute created and default set to 0. 
        self.served = 0

    def describe_restaurant(self):
        """Simple return of the attributes of the restaurant."""
        print(f"Welcome to the {self.name}! We serve {self.cuisine} food.")

    def open_restaurant(self):
        """Simple message to indicate that a restaurant is open"""
        print(f"The {self.name} is now open!")

    def number_served(self):
        """Prints the number of customers served"""
        print(f"Congrats! We have served {self.served} customers.")

    def set_number_served(self, base_served):
        """Setting the number of customers that have been served"""
        if base_served >= self.served:
            self.served = base_served
        else:
            print("Please do not enter a lower number of customers we have served.")

    def increment_number_served(self, todays_customer_count):
        """Simply adds todays number of customers served to the total of customers served"""
        self.served += todays_customer_count


# Test checks 
restaurant = Restaurant("Silly Chilly", "Mexican")
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served()
restaurant.set_number_served(10)
restaurant.set_number_served(5)
restaurant.number_served()
restaurant.increment_number_served(15)
restaurant.number_served()