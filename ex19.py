# Define a function called cheese_and_crackers to take 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print 2 f-strings which includes these arguements
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    # Print a blank line at the end of the final line
    print("Get a blanket.\n")

# Print a line of text to the screen
print("We can just give the function numbers directly:")
# Call function cheese_and_crackers, passing 20 and 30 as the two arguments
cheese_and_crackers(20, 30)

# Print a line of text to the screen
print("OR, we can use variables from our script:")
# Assign two variables to integer values
amount_of_cheese = 10
amount_of_crackers = 50

# Call the cheese_and_crackers function and pass the 2 variables defined above as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print a line of text to the screen
print("We can even do math inside too:")
# Call the cheese_and_crackers function, passing 2 mathematical expressions as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# Print a line of text to the screen
print("And we can combine the two, variables and math:")
# Call the cheese_and_crackers function, passing a combination of variables and mathemetical expressions as the 2 arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# As part of the study drill, define my own function and call it 10 different ways
def matt_function(x, y, z):
    print(f"The value of the first argument is: {x}!")
    print(f"The value of the 2nd argument is: {y}!")
    print(f"The value of the 3rd argument is: {z}!\n")
    return 35

print("Executing Matt's test function...")
matt_function(12, 45, 67)
matt_function(45 / 5, 64 % 10, 3 ** 4)
x = "Test"
matt_function(x, 11, 10000)
matt_function(x, "Matt's test string", len(x))
matt_function(list(range(10)), True, [1, 45, 10])
matt_function(list(range(1, 21, 3)), 45.3, "more text")
matt_function("abcdef"[1:3], "another string", 5)
matt_function(matt_function(3, 4, 5), 45, 90)
matt_function({"Matt" : 43, "Tom" : 41}, "Hartley", 7)
matt_function(45 < 90, -98 < -90, False)
