# Assign 10 to types_of_people
types_of_people = 10

# Assign an f-string to variable x and insert the types_of_people variable in the string
# Note, the variable must be defined before it's referenced, even if not being printed
x = f"There are {types_of_people} types of people."

# Assign the string 'binary' to the binary variable
binary = "binary"
#Assign the string "don't" to the do_not variable
do_not = "don't"
# Assign the f-string to the variable y and insert the variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# Print the x and y f-string variables
print(x)
print(y)

# Print 2 f-string strings, including the x and y f-strings
print(f"I said: {x}")
print(f"I said: '{y}'")

# Assign hilarious as a boolean variable and set it to False
hilarious = False

# Assign joke_evaluation variable to a string that includes an empty variable container.  Note, this is not an f-string.
joke_evaluation = "Isn't that joke so funny?! {}"

# Prints the joke_evaluation string with an empty variable container
print(joke_evaluation)
# Print the joke_evluation string and use the format() function to specify the variable to be in included in the variable container
print(joke_evaluation.format(hilarious))
# Print the string with an empty variable container and insert variable value with format function
print("Is this hard? {}".format(hilarious))

# Define 2 more strings
w = "This is the left side of..."
e = "a string with a right side."

# Print the concatenation of the 2 strings, using a '+' to join them
print(w + e)
