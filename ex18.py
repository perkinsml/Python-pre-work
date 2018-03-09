# Define a function that takes *args, unpacks them and prints them to the screen.  This is very similar to the argv command.
def print_two(*args):                       # *args tells Python to take the arguments to the function and then put them in args as a list.  Note, this does not allow a limitless number of fucntion arguments.
    arg1, arg2 = args                       # Unpack the args and assign them to 2 variables
    print(f"arg1: {arg1}, arg2: {arg2}")    # Print the vsariables using an f-string

# Define a funtion that takes and prints 2 variables without the need to unpack them - more efficient!
# This format is also more explicit about what the function accepts as arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# Define a function that accepts 1 argument and prints this to the screen
def print_one(arg1):
    print(f"arg1: {arg1}")

# Define a function that accepts no arguments and prints a message to the screen
def print_none():
    print("I got nothin'.")

# Call each of the functions with the required number of arguments
print_two("Matt", "Perkins")
print_two_again("Matt", "Perkins")
print_one("First!")
print_none()
