# Lets work with inheritance now we know the basic understanding of a class.
    # "Inheritance" is when a subclass (child class) take on the properties of 
        # the superclass (parent class)
    # Lets continue to use the Car class from the previous lesson, and build another class on top
        # of it. We will create a child class and name it Electric_car. Since it is still a car 
        # it will still have all the same attributes from the Car class. 

class Car:
    """A simple attempt to represent a car."""
    # All cars have the same attributes so we can also use these in Electric_car. 
    def __init__(self, make, model, year):
        """Initialize the attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    # We can also use all of these functions as well as they are just general information as well. 
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
        
# To make a subclass (child class) it will be the exact process as before, the only difference is
    # that a child class must be after its parent class. As python reads from top to bottom if the
    # the child class comes first, then there is nothing for the child class to reference to. 
class Electric_car(Car):
    # Here ---------^ we see how the child class references the parent class above. 
    """ Represent aspects of a car, specific to electric vehicles. """
    