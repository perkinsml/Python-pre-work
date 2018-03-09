# Welcome to Matt's Python Cheat Sheet, covering
# file input and output (this file needs a command line input to run),
# functions
# Note, refer to ex17.py for copying or appending contents of one file to another

from sys import argv
from os.path import exists

script, filename = argv
f = open(filename)
print(f"Here's your file {filename}:")
print(f.read())
f.close()

f = open(filename, 'w')
l1 = "Matt"
l2 = "is"
l3 = "great"

f.write(f"\n{l1}\n{l2}\n{l3}")


print("FUNCTIONS!")
def f1(*args):                              # *args tells Python to take the arguments to the function and then put them in args as a list.  Note, this does not allow a limitless number of fucntion arguments.
    arg1, arg2 = args                       # Unpack the args and assign them to 2 variables
    print(f"arg1: {arg1}, arg2: {arg2}")    # Print the vaariables using an f-string

def f2(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

f1("Matt", "Perkins")
f2("Matt", 43)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    test = crates / 2
    return jelly_beans, jars, crates   # Return jelly_beans, jars and crates variables
start_point = 10000
# Assign beans (5000000), jars (5000.0) and crates (50.0) to the values respective values returned by the secret_formula function
beans, jars, crates= secret_formula(start_point)
print("With a starting point of: {}".format(start_point))
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")
list_return = secret_formula(200)
print(list_return)
print("We'd have {} beans, {} jars, and {} crates.".format(*list_return))
