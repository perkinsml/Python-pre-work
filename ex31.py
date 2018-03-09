# Print a statement across 2 lines of text that requests input
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")
# Prompt for user input and store the response in the door variable
door = input("> ")
# If the response is door 1, execute the following block of code
if door == "1":
    # Print text, requesting a user response to the bear
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    # Prompt for user response to the bear, and store it in the bear variable
    bear = input("> ")
    # Print a statement, contingent on the bear response
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        # If the response to the bear wasn't one of those requested, print a catch-all statement
        print(f"Well doing {bear} is probably better.")
        print("Bear runs away.")
# If the response is door 2, execute the following block of code
elif door == "2":
    # Print 4 lines of text
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yello jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    # Prompt user for a response and store it in the insanity variable
    insanity = input("> ")
    # If the response was 1 or 2, execute the following code
    if insanity == "1" or insanity =="2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    # If the response wasn't a 1 or 2, use the catch-all below to execute this code
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
# If the user didn't enter door 1 or door 2 as a response to the initial question, execute the catch-all below
else:
    print("You stumble around and fall on a knife and die.  Good job!")
