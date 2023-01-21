# Now we have the base of our class lets add a default value for an attribute.
    # We are going to add an attribute called odometer_reading and set its value to 0.
    # Also lets create a method read_odometer() to report back its current reading.

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

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()