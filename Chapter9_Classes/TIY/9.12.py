# Here we split the admin module into 2 separate modules. user and privileges
    # Lets import both and user them to create another admin user for testing.
from privileges import Admin

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