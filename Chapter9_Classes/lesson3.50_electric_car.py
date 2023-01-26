# Lets try to override a parent method in the child class. 
    # Typical cars still use gasoline to run the engine, as such they need gas tanks.
    # Lets create a method in the Car class called fill_gas_tank() and when called it 
        # will print "The gas tank has been filled."

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

    def fill_gas_tank(self):
        """Simulate a command to fill the gas tank to a car."""
        print(f"The gas tank has been filled.")

# However electric cars do not have gas tanks so lets override the fill_gas_tank method to print
    # "This car does not have a gas tank to fill."
class Electric_car(Car):
    
    """ Represent aspects of a car, specific to electric vehicles. """
    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print(f"This car does not have a gas tank to fill.")

my_tesla = Electric_car("tesla", "model 3", 2019)
my_tesla.fill_gas_tank()