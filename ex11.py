# Prompt user to input age.  Including end = ' ' tells each print line to not end with a newline.
# Without the end=' ' at the end of the line, the response would be entered on the line after the question
print("How old are you?", end=' ')
# Assign input to age variable
age = input()
# Prompt user to input height.  Including end = ' ' prompts response on same line.
print("How tall are you (include units)?", end=' ')
# Assign input to height variable
height = input()
# Prompt user to enter weight.  Including end = ' ' prompts reponse on same line.
print("How much do you weight (include units)?", end=' ')
# Assign input to weight variable
weight = input()
# Promput user for favourite colour and store response directly in the colour variable
# Note, end = ' ' is not needed here to prompt for response on same line
colour = input("What is your favourite colour? ")

# Print f-string, including the 4 variables age, height, weight and colour
print(f"So you're {age} years old, {height} tall, {weight} heavy and your favourite colour is {colour}.")
# Print the same line of text, but without an f-string and using a format function
print("So you're {} year olds, {} tall, {} heavy and your favourite colour is {}.".format(age, height, weight, colour))
