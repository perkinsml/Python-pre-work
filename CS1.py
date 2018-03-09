# Welcome to Matt's Python Cheat Sheet, covering
# printing, formatting and user input

# Variable assignment
name = "Matt"
weight = 85
height = 180.0
x = f"Matt's weight is {weight}kgs."
hard = False
l = "Left"
r = "Right"
formatter = "{} {} {} {}"
months = "\nJan\nFeb\n\tMar\vApr"

# Printing
print("My name's Matt!")
print('I said, "do not touch this!\a"')
print()
print("Roosters:", 100 - 25 * 3 % 4)
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print(3 + 2 < 5 - 7)
print("Is 5 > -2?", 5 > -2)
print("Numbers:", 3 * -17, 5 % 2, "Text.", "More numbers:", 45 * 45)
print("Matt is", weight,"kgs.")
print(f"{name} is {height}cm tall.")
print(f"Is {name}'s height greater than his weight? {height > weight}.")
print(f"{name}'s weight divided by his height is: {round(weight/height,2)}.")
print()
print(x)
print(f"I said: {x}")
print("Is this hard? {}".format(hard))
print(formatter.format("mix", 4, True, 3.4))
print(l, r)
print(l + r)
print(l, end=' ')
print(r)
print("." * (4+6))
print()
print("Months: ", months)
print()

# User input
eyes = input("Eye colour? ")
age = input("Age? ")
print(f"You are {age} years old, with {eyes} eyes.")
print("You are {} years old, with {} eyes.".format(age, eyes))
