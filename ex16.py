# From the sys module, import argv (argument vector), enabling command line input
from sys import argv
# Unpack the argv list items to 2 variables
script, filename = argv
# Print a message referring to the filename variable input by the user
# Print a message that gives the user a choice to quit the program wth a keyboard interrupt, or continue to deletion
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# Prompt the user for their selection
input("? ")
# Print an update message to the screen
print("Opening the file...")
# Open the filename file in write mode and save the file object to target
# Note, in 'w' node the file doesn't need to pre-exist for this code to exist
target = open(filename, 'w')
# Print an update message
print("Truncating the file.  Goodbye!")
# Empty the file object of its contents.  This line of code isn't actually necessary when the file is opened in 'w' mode
target.truncate()
# Print an update message
print("Now I'm going to ask you for three lines.")
# Prompt the user to provide 3 lines of input and store these in line1, line2, and line3 variables
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
# Print an update message
print("I'm going to write these lines to the file.")
# Write each of the 3 variables (line1, line2, and line3) to the file, separating each with a new line
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Now I'll write to the file in more efficient way!")
target.write(f"{line1} \n{line2} \n{line3} \n")
# Print an update message before closing the file object, which enables the contents to be written to the file itself
print("And finally, we close it.")
target.close()
