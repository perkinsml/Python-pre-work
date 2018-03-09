# Assign 3 variables
people = 30
cars = 40
trucks = 15

# Compare the values of the cars and people variables and print the appropriate statement
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
# Compare the trucks and cars variables and print the appropriate statement
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
# Compare the people and trucks variables and print the appropriate statement
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
