# Define a function that accepts a string and splits it using a space as the delimiter
# Return a list of words
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# Define function that takes a list and returns an alphabetically sorted list
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# Define a function that takes a list, and removes and returns the first item in that list
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

# Define a function that takes a list, and removes and returns
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

# Define a function that take a string, splits it using break_words and assigns it to the words list
# then returns the words lists sorted alphabetically using the sort_words function
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# Define a function that takes a sentence, splits the sentence into a list of individual words,
# and then prints the first and last words within the words list
def print_first_and_last(sentence):
    """Prints the first and last word of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# Define a function that take a sentence, breaks it into a list of individual words sorted alphabtecally,
# the prints the first and last words of this sorted words list
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
