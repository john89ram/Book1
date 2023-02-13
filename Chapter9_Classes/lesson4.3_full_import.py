import lesson4_car
# Be sure when you import the entire module that you use dot notation to call methods.
    # Dot notation uses module_name.ClassName(), lets practice here.
    # This can help with naming and less mess ups.

my_beetle = lesson4_car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = lesson4_car.Electric_car('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# You can also import all Classes in a module by using
    # "from module import *" 
    # This way you can continue to program as we did earlier without the dot notation.