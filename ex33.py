# Create an empty list called numbers
numbers = []

# Define a function that take a single argument x and iterates through a while loop (x - 1) times
def list_generator(x, increment):
    # Assign i the value 0
    i = 0
    # While i is less than x, execute the block of code
    while i < x:
        # Print the value of i at the beginning of the while loop
        # Append i to the numbers list
        print(f"At the top i is {i}")
        numbers.append(i)
        # Increment the value of i by 1
        i += increment
        # Print the numbers list
        print("Numbers now: ", numbers)
        # Print the value of it at the end of the while loop, following the increment in its value
        print(f"At the bottom i is {i}")

# Call the list_generator function
list_length = int(input("How many elements in the list? "))
increment = int(input("What increment would you like? "))
list_generator(list_length, increment)

# Print a line of text
print("The numbers: ")
# Iterate through each item in the numbers list and print it
for num in numbers:
    print(num)

# Let's generate the list using a for loop:
numbers1 = []
for i in range(0, list_length, increment):
    numbers1.append(i)
print(f"The list generated with the For loop is {numbers1}.")
