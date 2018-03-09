# Print string "Mary had a little lamb."
print("Mary had a little lamb.")
# Print a string with a variable container and use the format function to include 'snow' in that variable container'
# The string included in the format function can have single or double quotes
print("Its fleece was white as {}.".format("snow"))
# Use an f-string to print exactly the same line as the text above
print(f"Its fleece was white as {'snow'}.")
# Print the string "And everywhere that Mary went"
print("And everywhere that Mary went.")
# Print 10 dots on the same line.  This multiplication can be any type of mathematical expression.
# Multiplying a string by a number repeats the string by that number
print("." * (4+6))

# Assign variables to a letter
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Print a concatentation of string variables end1...end6,
# followed by the variable 'end', which enables print statements to continue without a line break.
# Note, end = ' ' inserts a space between the letters, but the value of end can be any None or String value
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
# On the same line, print the concatenation of the end7...end 12 strings
print(end7 + end8 + end9 + end10 + end11 + end12)
