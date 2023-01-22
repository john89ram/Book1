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
        #self.odometer_reading = mileage
    # Here is an extended option with some logic to prevent users to turn back the mileage.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You  can't roll back back an odometer!")

    # 3 Let show the last example by adding "miles" by increments to the current mileage. 
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

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

# Extended mileage check (enter mileage under the current mileage, result should trigger else)
my_new_car.update_odometer(12)

# Ex. 3
    # With the increment method we just created lets add 100 miles to our current mileage.
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()