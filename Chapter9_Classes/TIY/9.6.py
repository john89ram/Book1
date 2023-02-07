# Ice Cream Stand - An Ice cream stand is a specialized type of restaurant. Write a child class
    # called IceCreamStand that inherits from the Restaurant class from exercise 9.1 or 9.4. 
        # Add an attribute called "flavors" that stores a list of ice cream flavors. 
        # Then create a method that displays these flavors. 
        # Lastly create an instance of IceCreamStand, and call the method.

class Restaurant:
    """ A simple class to create a restaurant and accepting the attributes name and cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes of the restaurant"""
        self.name = restaurant_name
        self.cuisine = cuisine_type
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

class IceCreamStand(Restaurant):
    """ A child class to simply explain a Ice Cream Stand """

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """Initialize the attributes of an Ice Cream Stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def list_flavors(self):
        """Print all flavors that """
        print(self.flavors)

dj_ice_cream_shop = IceCreamStand("DJ's Ice Cream Shop", "desert" ,"vanilla", "chocolate", "strawberry", "mint")
dj_ice_cream_shop.describe_restaurant()
dj_ice_cream_shop.open_restaurant()
dj_ice_cream_shop.list_flavors()