# From the sys module, import argv (arguement vector), enabling the user to specify input at the command line
# when they run the program
from sys import argv
# Expect 2 command line fields: script and the filename
# Unpack the argv list and assign the items to the variables script and filename
script, filename = argv
# Open filename and assign the file object to txt
txt = open(filename)
# Print a line of text that includes the filename
print(f"Here's your file {filename}:")
# Read file object txt and print its contents, and hence the contents of the file
print(txt.read())
# This time, ask the user for the name of the file while the script is running
print("Type the filename again: ")
# Store the name of the file in the file_again varibale
file_again = input("> ")
# Open the file and assign the file object to txt_again
txt_again = open(file_again)
# Read file object txt_again and print its contents, and hence the contents of the file
print(txt_again.read())
# Close the file objects.  It's always important to close these one you have finished with them.
txt.close()
txt_again.close()
