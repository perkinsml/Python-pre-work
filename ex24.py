# Print lines of text to the screen using the escape character (\) to print
# apostrophes, backslash, new lines (\n) and tabs (\t)
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ to do: ')
print('\n new lines and \t tabs.')

# Assign poem to a multi-line string using """ to extend the assignment across lines
# Within the string, include tabs (\t) and new lines (\n), with the final line
# starting on a new line, and a double tab
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires explanation
\n\t\twhere there is none.
"""
# Print the poem string to the screen
print("------------")
print(poem)
print("------------")

# Assign the variable five with a mathematical expression
five = 10 - 2 + 3 - 6
# Print a sentence to the screen, including the variable five using an f-string
print(f"This should be five: {five}")
# Define a function 'secret_formula' that takes a single argument and returns
# three variables assigned with mathematical expressions
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates    # Return jelly_beans, jars and crates variables
# Assign variable starting_point to 10000
start_point = 10000
# Call function secret_formula and pass it the start_point variable as the argument
# Assign beans (5000000), jars (5000.0) and crates (50.0) to the values respective values returned by the secret_formula function
beans, jars, crates = secret_formula(start_point)

# Remember that this is another way to format a string
# Print a string, referencing the start_point variable
print("With a starting point of: {}".format(start_point))
# It's just like with an f"" string
print(f"we'd have {beans} beans, {jars} jars, and {crates} crates.")

# Reassign the value of start_point (to 1000)
start_point = start_point / 10

print("We can also do that this way: ")
# Call function secret_formula with start_point = 1000 and
# assign the variables returned to the formula list
formula = secret_formula(start_point)
print(formula)
# This is an easy way to apply a list to a format string
# Print a string with variable placeholders populated by applying the format function to all items in the formula string
# Prints: We'd have 500000.0 beans, 500.0 jars, and 5.0 crates
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
