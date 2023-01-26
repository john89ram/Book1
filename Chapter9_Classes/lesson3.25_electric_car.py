# We can also add attributes and methods additional to child classes.
    # Unlike traditional cars, electric vehicles do not run on gas but on batteries.
    # Lets add an attribute to represent the size of the battery.  

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize the attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the current value of the odometer"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
    
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You  can't roll back back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Electric_car(Car):
    
    """ Represent aspects of a car, specific to electric vehicles. """
    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class """
        super().__init__(make, model, year)
        # Like normal we can just add the additional attributes here
        self.battery_size = 75

        # And lets add a method to display the batteries size
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

my_tesla = Electric_car("tesla", "model 3", 2019)
print(my_tesla.get_descriptive_name())
# Method test
my_tesla.describe_battery()