# Import argv from the sys module, enabling command line input
from sys import argv
# Import the exists command which returns True if a file exists and False if it doesn't
from os.path import exists
# Unpack the argv list and assign it to 3 variables: script, from_file and to_file
script, from_file, to_file = argv
# Print a message to explain copying content from 2nd argument to 3rd argument
print(f"Copying from {from_file} to {to_file}.")

# Open the from_file and store it in the in_file file object
in_file = open(from_file)
# Read the contents of in_file and save it indata
indata = in_file.read()
# Print a message to the screen that includes the length of the file in bytes
print(f"The input file is {len(indata)} bytes long.")
# Print a message to the screen that displas whether the new file already exists
print(f"Does the output file exist? {exists(to_file)}")
# Print a message to the screen asking if the user wishes to continue, and provide the option to keyboard interrupt and exit the program
print("Ready, hit RETURN to continue, or CTRL-C to abort.")
# Wait for user input
input()
# Create or open the new file and assign it to the out_file object
# Open it in append mode to enable existing content to be added to, rather than overidden
out_file = open(to_file, 'a')
# Write the contents of indata to the out_file object
out_file.write(indata)
# Print an update message
print("Alright, all done.")
# Close both files
out_file.close()
in_file.close()
