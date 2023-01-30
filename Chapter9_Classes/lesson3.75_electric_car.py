#  Sometimes when creating your class, they can become too large and be overly complicated to read.
    # To reduce the confusion you can create sub-classes and break down the attributes complexity.
    # Lets use the class Electric car, and the different types of batteries that are used when 
    # creating an electric car. 
        # We will create a sub-class called Battery and further explain electric call batteries. 
        
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

# Since this class does not need to inherit traits from the parent class we can create it anywhere
    # in our program. 
class Battery:
    """ A simple attempt to model a battery for an electric car. """
    # As before we still need to initialize the class and plug our instance.
    # Since the default size of Tesla cars are 75kWh we can set that here. 
    def __init__(self, batter_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = batter_size
    # Since we created a battery class lets take the describe_battery() method and move it here. 
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")
        
    # Lets continue to add on to this create an if statement if we need to need to change our 
        # battery size. 
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
    
class Electric_car(Car):
    
    """ Represent aspects of a car, specific to electric vehicles. """
    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class """
        super().__init__(make, model, year)
        #Now we can just enter that instance here as an attribute.
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars do not have gas tanks."""
        print(f"This car does not have a gas tank to fill.")

my_tesla = Electric_car("tesla", "model 3", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()