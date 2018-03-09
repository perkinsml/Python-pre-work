# Assign formatter variable to a string with 4 variable containers and a space between them
formatter = "{} {} {} {}"
# Print the formatter string, and insert 1, 2, 3 and 4 into the variable containers
print(formatter.format(1, 2, 3, 4))
# Print the formatter string and insert 'one', 'two', 'three' and 'four' into the variable containers
print(formatter.format("one", "two", "three", "four"))
# Print the formatter string and insert 4 Boolean keywords into the 4 variable containers
print(formatter.format(True, False, False, True))
# Print the formatter string and include the formatter string (with its 4 variable containers) into the 4 variable containers
print(formatter.format(formatter, formatter, formatter, formatter))
# Print the formatter string and include the 4 strings below in the 4 variable containers
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
# Print the formatter string and include the formatter string in its 4 variable containers.
# This time include some values in 2 of the formatter strings
print(formatter.format(formatter.format(1, 2, 3, 4), formatter.format("mix", 4, True, 3.4), formatter, formatter))
