# Import argv (arguement vector) from the sys module
# This enables a user to provide input from the command line
from sys import argv
# script is the name of the Python file to be executed, and is hence the first variable
# Enable user to specify 3 additional variables at the command line
# As demonstrated from the print command below, this stores all input as a list
print("argv = ", repr(argv))
# Unpack the list and assign the items to the script, first, second and third variables
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third vairable is:", third)

an_input = input("And now I want input while the script is running: ")
print(f"Your input was {an_input}!")
