# From the sys module import the exit function
from sys import exit

# Define the gold_room function, which request the user for input and envokes the relevant response
def gold_room():
    print("This room is full of gold.  How much do you take?")
    # Prompt the user for input
    choice = input("> ")
    # If 0 or 1 is contained within the user's response, convert the string to an integer and assign the value to how_much
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    # If 0 or 1 is not contained within the user's reponse, call the dead function with an appropriate string
    else:
        dead("Man, learn to type a number.")
    # If how_much is less than 50, print a message and exit Python
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    # If how_much is greater than or equal to 50, call the dead function with an appropriate string message
    else:
        dead("You greedy bastard!")

# Define a function bear_room
def bear_room():
    # Print text to the screen
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # Assign bear_moved to False
    bear_moved = False
    # Always execute the code block within the while loop when the bear_room function is called
    # This is an infinite while loop which is only exited by calling the dead function, which contains an exit function call
    while True:
        # Prompt user for a response to the question asked in the function's text above
        choice = input("> ")
        # If response is 'take honey', the dead function is envoked with a string argument
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # If response is 'taunt bear' and bear_moved = False, print text to screen and set bear_moved to True
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
        # If response is 'taught bear' and bear_moved = True, envoke the dead function with an appropriate string argument
            dead("The bear gets pissed off and chews your leg off.")
        # If response is 'open door' and bear_moved = True, call the gold_room function
        elif choice == "open door" and bear_moved:
            gold_room()
        # If response isn't 'taunt bear' or 'open door', print a catch-all error message and repeat the while loop
        else:
            print("I got know idea what that means.")

# Define the cthulhu_room function, which starts by printing text and requesting a repsonse from the user
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")
    # Prompt for response from user and assign it to choice
    choice = input("> ")
    # If 'flee' contained wthin user response, re-start the game by calling the start function
    if "flee" in choice:
        start()
    # If 'head' is contained within user response, call the dead function with an approriate string message
    elif "head" in choice:
        dead("Well that was tasty!")
    # If the user response doesn't contain 'flee' or 'head', call this function again
    else:
        cthulhu_room()

# Define a function (dead) which takes a string as an argument
def dead(why):
    # Print the argument to the screen, combined with 'God job!'
    print(why, "Good job!")
    # Exit from Python
    exit(0)

# Define the start function, which begins by prompting you to choose the 'left' or right' door
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    # Prompt user for input
    choice = input("> ")
    # If choice is 'left', call the bear_room function
    if choice == "left":
        bear_room()
    # If choice is 'right', call the cthulhu_room function
    elif choice == "right":
        cthulhu_room()
    # If choice is neither 'left' or 'right', call the dead function with a string as an argument
    else:
        dead("You stumble around the room until you starve.")

# Play this stupid game by calling the start function
start()
