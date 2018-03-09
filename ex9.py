# Assign days variable to the string "Mon....Sun"
days = "Mon Tue Wed Thu Fri Sat Sun"
# Assign months variable to the string with month Jan...Aug, separated with a \n, which prints a line break
months = "Jan\nFeb\nMar\nAp\nMay\nJun\nJul\nAug"

# Print "Here are the days: ", followed by the days variable
print("Here are the days: ", days)
# Print "Here are the months: " followed by the months variable,
# which include Jan on the same line, but each subsequent month on a new line due to the \n in the string
print("Here are the months: ", months)
# Print a multi-line string. The triple-quotes enables the string to be defined over multiple lines
# The string will be printed with the same formatting included in the string.
# A double quote will not allow multi-line definition.
print("""
There's something going on here.
    With the three double-quotes.
We'll be able to type as much as we like.
        Even 4 lines if we want,
or 5,
or 6""")
