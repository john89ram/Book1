# Login Attempts - Copy the exercise from 9.3.
    # Add an attribute called login_attempts
    # Write a method called increment_login_attempts() that increases the value of login_attempts
    # Write another method called reset_login_attempts() that resets the value of login_attempts
        # Now make an instance of the User class and call the increment_login_attempts()
        # Be sure to print the login_attempts to track that the method is working properly.
        # The call reset_login_attempts() to bring the login_attempts to 0.
        
# Copy exercise 9.3
class User:
    """A little more complicated class that stores attributes that describes a user"""

    def __init__(self, first_name, last_name, age, robot_status, email):
        """Attributes for typical user information"""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.robot = robot_status
        self.email = email
        # Create an attribute called login_attempts
        self.login_attempts = 0

    def describe_user(self):
        """Prints all information saved on a user"""
        print(f"First Name:{self.first}"
                f"\nLast Name:{self.last}"
                f"\nAge:{self.age}"
                f"\nEmail:{self.email}"
                f"\nRobot:{self.robot}")

    def greet_user(self):
        """Simple greeting to newly added user"""
        print(f"\nHello {self.first} {self.last}! Welcome to our site. Please let us know if we need to change any of your data below.")
    
    def read_login_attempts(self):
        """ Print out the number of login attempts made"""
        print(f"You have tried to login {self.login_attempts} times.")
        
    # Create a method called increment_login_attempts()
    def increment_login_attempts(self, login_number):
        """ A function that increases the value of login_attempts """
        self.login_attempts += login_number
    
    # Create a method to reset the number of login_attempts
    def reset_login_attempts(self):
        """ A function to reset the value of login_attempts to 0 """
        self.login_attempts = 0
        
user1 = User("John", "Smith", 30, "No", "johnsmith@example.com")
user1.describe_user()
user1.read_login_attempts()
user1.increment_login_attempts(3)
user1.read_login_attempts()
user1.increment_login_attempts(5)
user1.read_login_attempts()
user1.reset_login_attempts()
user1.read_login_attempts()
