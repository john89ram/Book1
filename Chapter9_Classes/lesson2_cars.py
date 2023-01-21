# Lets create a new class that we can practice modifying. 
    # Here we will create a simple class that have attributes that describes the car.
    # Lets start with 3 attributes make, model, & year.

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize the attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())