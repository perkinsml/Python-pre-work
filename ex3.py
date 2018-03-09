# Print the line of text
print("I will now count my chickens:")

# Print the number of Hens (30.0).
# Note, the division is executed first by order of operations.
# Division always returns a floating point number, so the result is a floating point.
print("Hens", 25 + 30 / 6)

# Print the number of roosters (97).  Note, 25 * 3 % 4 = 3. and is executed first.
print("Roosters", 100 - 25 * 3 % 4) #Note % has same precedence as * and /

# Print the line of text
print("Now I will count the eggs:")

# Print the result of the sum below (6.75).  Note % and division are performed first.
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Print the line of text
print("Is it true that 3 + 2 < 5 - 7?")

# Prints False becase 5 is not less than -2
print(3 + 2 < 5 - 7)

# Prints the text with the result of the sum (5)
print("What is 3 + 2?", 3 + 2)

# Prints the text with the result of the sum (-2)
print("What is 5 - 7?", 5 - 7)

# Print the line of text
print("Oh, that's what it's False.")

# Print the line of text
print("How about some more.")

# Print the line of text, with True at the end
print("Is it greater?", 5 > -2)

# Print the line of text, with True at the end
print("Is it greater or equal to?", 5 >= -2)

# Print the line of text with False at the end
print("Is it less or equal", 5 <= -2)
