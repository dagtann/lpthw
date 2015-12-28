# Variable and names
# This ex shows how to define variables

# Variable definitions
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Messages
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "people to pool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Shorthand reference for variables
# -> format string
print "There are %d cars driven." % cars_driven