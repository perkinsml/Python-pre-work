# Prompt user for age, height, weight and colour and assign directly to a variable
# Convert the age to an integer so you can manipulate the value in a later statement
age = int(input("How old are you? "))
# Include the age variable in the input sentence, printed as an f-string
height = input(f"You're age? {age}.  Cool! How tall are you (include units)? ")
# Include a calculation on the age variable and include it in the f-string prompting the input of weight
weight = input(f"Did you know that your age in dog years is {age / 7}? How much do you weigh (include units)? ")
colour = input("What is your favourite colour? ")

# Print the f-string with the 4 variables above
print(f"So, you're {age} years old, {height} tall, {weight} heavy and your favourite colour is {colour}.")
print("So, you're {} years old, {} tall, {} heavy and your favourite colour is {}.".format(age, height, weight, colour))
