cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

# test = carpool_capacity_test / passengers # to replicate the error for study drill

# Traceback (most recent call last):
#   File "E:\Labs\NewHope\PythonRefresher\hardWay\ex4.py", line 10, in <module>
#     test = carpool_capacity_test / passengers
#            ^^^^^^^^^^^^^^^^^^^^^
# NameError: name 'carpool_capacity_test' is not defined. Did you mean: 'carpool_capacity'?


print("there are", cars, "cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driven, "empty cars today")
print("we can transport", carpool_capacity, "transport today in carpool")
print("we have", passengers, "for carpool today")
print("We need to put about", average_passenger_per_car, "in each car")
