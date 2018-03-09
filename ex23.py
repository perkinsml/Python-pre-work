# Perform a generic import of the sys module i.e. without specifing a command, function or variable to import from the module
import sys
# Since argv wasn't specifically imported, it needs to be accessed via dot notation
# Unpack and assign the 3 variables supplied on the command line: script, input_encoding and error
script, input_encoding, error = sys.argv
# Define a function 'main' which accepts 3 arguments: a file_object, and 2 additional arguments supplied on the command line
# at the time of running the script - the encoding and the error handling approach
def main(language_file, encoding, errors):
    # Read the first line of the file object and assign it to the variable line
    line = language_file.readline()
    # If line has something in it, the if condition will be true and code within the if condition will be executed
    # The readline function will only return an empty string at the end of the file,
    # so the code in the if statement will run to the end of the file
    if line:
        # Call the function print_line, passing it the line of text, and the encoding and errors variables
        print_line(line, encoding, errors)
        # Call the function again, and continue to loop through the file
        return main(language_file, encoding, errors)

# Define a function 'print_line' that takes a line of text, and the specified encoding and errors variables
# DBES: Decode Bytes, Encode String
def print_line(line, encoding, errors):
    # Strip the white space from the end of the line string (i.e. the trailing \n)
    next_lang = line.strip()
    # Encode the string into raw bytes.  Pass the function the desired encoding and Python error handling approach.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    print(raw_bytes)
    print(type(raw_bytes))
    # Take the raw bytes and apply the decode function to get the string in the encoding format specified (UTF)
    # Note, cooked_string is the same as next_lang.  This line of code simply shows the reverse of the line above.
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # Print the raw_bytes and cooked_string to the screen to display them
    print(raw_bytes, "<===>", cooked_string)

# Open file 'languages.txt' and assign it to the 'languages' file object.  Specify the encoding as UTF-8, as some computers use a different encoding default.
languages = open("languages.txt", encoding="utf-8")
# Call the main function, and pass it the languages file object, along with the input_encoding and
# error arguments entered on the command line
main(languages, input_encoding, error)
