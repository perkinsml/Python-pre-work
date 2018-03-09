# From the sys module, import command argv enabling command line input when the script is executed
from sys import argv
# Unpack 2 command line inputs and assign them to the variables: script and input_file
script, input_file = argv
# Define a function that takes a file object argument and prints its contents
def print_all(f):
    print(f.read())
# Define a function that takes a file object argument and moves the read/write location to the beginning of the file
def rewind(f):
    f.seek(0)
# Define a function that takes 2 arguments and prints a line number, followed by a single line of text from a file object argument
# Note, this function does not print the text AT the line_count!
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")       # Adding end = "" at the end of this print statement stops print inserting a line space between the lines of text
# Open file input_file in read only mode (the default) and assign the file object to current_file
current_file = open(input_file)

# Print a line of text to the screen
print("First let's print the whole file:\n")
# Call the print_all function and pass the current_file file object as the argument
print_all(current_file)
# Print a line of text to the screen
print("Now let's rewind, kind of like a tape.")
# Call the rewind function and pass the current_file file object as the argument
# Without the rewind, the print_a_line function will read from the current location, which is the end of the file after the print_all function call
rewind(current_file)
# Print a line of text to the screen
print("Let's print 3 lines:")
# Set the variable current_line equal to 1
current_line = 1
# Call the print_a_line function and pass the current_line variable and current_file file object as arguments
print_a_line(current_line, current_file)
# Incerement the current_line variable and print the next 2 lines of text by calling the print_a_line function
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
