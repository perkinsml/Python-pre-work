# Assign 3 lists: the_count, fruits and change
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This type of for loop goes through all items in the_count list
for number in the_count:
    # For each list item, print an f-string that includes the list item
    print(f"This is count {number}.")

# Same as above.  For each item in the fruits list, print it in an f-string
for fruit in fruits:
    print(f"A fruit of type {fruit}.")

# Also, we can go through mixed lists too:
# Notice we have to use {} since we don't know what's in it
# For each item in the change list, print it in an f-string
for i in change:
    print(f"I got {i}.")

# We can also build lists.  First start with an empty one.
elements = []

# Use the range function to do 0 to 5 counts
for i in range(0, 6):
    # Print a statement for each iteration of the loop that includes the loop counter
    print(f"Adding {i} to the list.")
    # Append the loop counter as an item to the elements list
    elements.append(i)

# An alternative to creating a list without the for loop
# Note, list must be around the range function for it to return a list
elements1 = list(range(40, 50, 2))
print(f"Contents of elements1: {elements1}.")


# We can print the element list items individually too
for i in elements:
    print(f"Element was: {i}.")
