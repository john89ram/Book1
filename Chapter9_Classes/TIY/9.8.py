# Privileges - Write a separate Privilege class. The class should have one attribute 'privileges'. 
    # This should store a list of strings as described in 9.7
    # Move the show_privileges() method to this class. 
    # Make a Privileges instance as an attribute in the Admin class. 
    # Create a new instance of Admin and use your method to show its privileges.
    
  
class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
            
class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        # Here we link the Privilege class to the Admin class, breaking down code can make it
            # easier to understand. However try to keep it clean and not over explain. 
        self.privileges = Privileges()

class Privileges:
    """ A class to hold all the privileges that a user might have. """
    def __init__(self, privileges=[]):
        # Initialize the privilege attribute and set it as an empty list.
        # Take care on how to name your attributes as this example will cause you to call this
            # attribute twice. ex - username.privileges.privileges() - can be confusing.
        self.privileges = privileges
    
    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print(f"- This user has no privileges.")
            
john = Admin('john', 'ramirez', 'jramirez', 'jramirez@fakeemail.com', 'Texas')
john.describe_user()

john.privileges.show_privileges()

john_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
john.privileges.privileges = john_privileges
john.privileges.show_privileges()