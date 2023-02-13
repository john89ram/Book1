# Imported Admin - Create another module of 9.8 and called it Admin so we can import it.
    # Create an an admin to make sure we were able to import everything correctly.
from admin import Admin, User, Privileges

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