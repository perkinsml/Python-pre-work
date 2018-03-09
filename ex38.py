# Define a string: ten_things
ten_things = "Apple Oranges Crows Telephone Light Sugar"
# Print a line of text to the screen
print("Wait, there are not 10 thinhgs in that list.  Let's fix that.")
# Convert the ten_things string into a list, using the space between the words as the delimiter
stuff = ten_things.split(' ')
# Define a list: more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
            "Banana", "Girl", "Boy"]
# Loop through stuff based on its length, which starts at 6
while len(stuff) != 10:
    # Pop the last item of the more_stuff list and assign it to variable next_one
    next_one = more_stuff.pop()
    # Print a statement to the screen that inludes next_one, popped from the more_stuff list
    print("Adding: ", next_one)
    # Append next_one to the stuff list
    stuff.append(next_one)
    # Print the new length of the stuff list
    print(f"There are {len(stuff)} items now")
# Print a statement to the screen that includes the new stuff list with 10 items
print("There we go: ", stuff)
# Print a statement to the screen
print("Let's do some other things with stuff")
# Print the item at position 1 in the stuff list
print(stuff[1])
# Print the last item in the stuff list
print(stuff[-1])    # Whoa! fancy
# Print the popped item from the end of the stuff list
print(stuff.pop())
# Print the space joined with stuff list items
print(' '.join(stuff))
# Print the # joined with stuff list items at positions 3 and 4
print('#'.join(stuff[3:5]))
