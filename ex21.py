# Define a function (add) that takes two arguements, prints a line of text referenceing them
# and then returns the addition of the two arguments
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
# Define a function (subtract) that takes two arguments, prints a line of text referencing them
# and then returns the subtraction of the 2nd argument from the first
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
# Define a function (multiply) that takes two arguments, prints a line of text referencing them
# and then returns the products of the two arguments
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
# Define a function (divide) that takes two arguments, prints a line of text referencing them
# and then returns their quotient
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# Print a line of text
print("Let's do some math with just functions!")
# Set four variables to the return values of the functions with the values specified in the function calls below
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# Print a sentence referencing the 4 varaiables assigned the return values of the function calls above
print(f" Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# Print a line of text to the screen
print("Here is a puzzle.")
# Assign the what variable to the return value of the add function, with the arguments:
# age (= 35) and the return of the subtract function, passed the height and multiply return values
# which is passed the weight and return values of the divide function, which is passed the iq variable and 2!
# what = add(35, subtract(74, multiply(180, divide(50,2)))) = 4391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# Print a line of text to the screen that references the what variable
print("That becomes: ", what, "Can you do it by hand?")
