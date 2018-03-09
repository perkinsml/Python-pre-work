# From the sys module, import argv (arguement vector) which enables users to provide input at the command line
from sys import argv

# Unpack the argv list and assign the items to the script, user_name and colour variables
script, user_name, colour = argv
# Set the value of the prompt that will be used to request additional user input
prompt = "---> "

# Print text using variables provided at the command line
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
# Request additional input from the user after running the script and store it in the likes variable
print(f"Do you like me {user_name}?\n")
likes = input(prompt)
# Request additional input from the user after running the script and store it in the lives variable
print(f"Where do you live {user_name}?")
lives = input(prompt)
# Print a line of text that references a variable provided at the command line
print(f"I already know your favourite colour is {colour}!")
# Request additional input from the user after running the script and store it in the computer variable
print("What kind of computer do you have?")
computer = input(prompt)
# Print multiple lines of text, referencing both command line and script variables
print(f"""Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.  Nice!
I bet it's {colour} too!
""")
