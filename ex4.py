# Set the value of my variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# Derive values based on the variables above
# Calculate the number of cars not driven and driven, assuming that the number of drivers is equivalent to the number of cars driven
cars_not_driven = cars - drivers
cars_driven = drivers
# Calculate the carpool capacity as the number of cars driven multiplied by their space
carpool_capacity = cars_driven * space_in_a_car
# Calculate the average number of passengers per car by dividing the total number of psasengers by the number of cars driven
average_passengers_per_car = passengers / cars_driven

# Print statements about the data using the variables above
print("There are ", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("we need to put", average_passengers_per_car, "in each car.")
