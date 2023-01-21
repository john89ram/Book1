# Not a lot of cars that are sold have 0 miles on it. 
    # So lets try to modify this attribute to something more realistic.
    # This can be resolved in 3 ways.
        # 1. Change the value directly through the instance.
        # 2. Set the value using the method.
        # 3. Change the value by increments (add to it). We will show all 3

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

    # 2 Set the value using the method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage
        
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 1. Change the value directly through the instance.
    # Ex. 1
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Ex. 2
my_new_car.update_odometer(45)
my_new_car.read_odometer()

 