# Users - Make a class called User. Create 2 attributes called.
    # first_name & last_name
    # afterwards you can create any other attributes that may be stored along with a user profile
    # Now make a method called describe_user() that prints a summary of the user's info.
    # Create another method called greet_user() that prints a greeting to the user.

class User:
    """A little more complicated class that stores attributes that describes a user"""

    def __init__(self, first_name, last_name, age, robot_status, email):
        """Attributes for typical user information"""
        self.first = first_name
        self.last = last_name
        self.age = age
        self.robot = robot_status
        self.email = email

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


user1 = User("John", "Smith", 30, "No", "johnsmith@example.com")
user2 = User("Jane", "Doe", 25, "No", "janedoe@example.com")
user3 = User("Robot", "1", 5, "Yes", "robot1@example.com")
user4 = User("Robot", "2", 7, "Yes", "robot2@example.com")
user5 = User("Robot", "3", 3, "Yes", "robot3@example.com")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()

user4.greet_user()
user4.describe_user()

user5.greet_user()
user5.describe_user()
