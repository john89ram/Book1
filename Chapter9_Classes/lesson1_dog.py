class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

# Now that we created a simple class with attributes (variables that 
    # are accessible through instances. Ex self.name & self.age) 
    # lets make a dog and test it out.

# Lets create a dog called Mocha and she is 10 y/o.
    # The first parameter "self" is not used and is automatically used to initiate the class.
    # So all that is needed are the other arguments "name" & "age"
my_dog = Dog('Mocha', 10)

# Lets call on these attributes by using the dot method. 
    # created_dog.requested_attribute
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

# Now we can also use the other functions that we have our dog programmed to do.
    # We can do this using the same dot method
my_dog.sit()
my_dog.roll_over()

# Here we will create another dog, "your_dog", and lets create some attributes from him.

your_dog = Dog("Boyd", 5)

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()