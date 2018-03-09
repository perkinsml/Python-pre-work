# A 'study drill script' to read the contents of a file and display the contents to the screen
from sys import argv
from time import sleep

script, filename = argv

print(f"Reading {filename}...")
sleep(2)
a_file = open(filename)
print(f"...and here are the contents of {filename}...")
print(a_file.read())
a_file.close()
