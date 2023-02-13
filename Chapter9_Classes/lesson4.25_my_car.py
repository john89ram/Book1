from lesson4_car import Car

my_car = Car("ford", "mustang", "1969")
print(my_car.get_descriptive_name())

my_car.update_odometer(20)
my_car.read_odometer()