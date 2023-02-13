from lesson4_car import Car, Electric_car
# Lets import multiple classes so we can use them.
    # Might be simpler to just import the full model but some can be very packed.

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = Electric_car('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())