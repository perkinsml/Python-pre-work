# Define a class named Song that is a object
class Song(object):
# Inititation function, which requires 2 arguments to instantiate an object
# Class Song has a __init__ that takes self, lyrics and rating parameters
    def __init__(self, lyrics, rating):
        self.lyrics = lyrics        # Assign the instance attributes
        self.rating = rating
# Class Song has a function that takes self parameters
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Set happy_birthday to an instance of class Song
happy_bday = Song(["Happy Birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"],2)
# Set bulls_on_parade to an instance of class Song
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"], 1)


matt_test = Song([5, 6, 7, 8, "My boot scooting baby"], 3)


x = "Hold on for one more day"
y = "I know that there is change"
z = "But you hold on for one more day"
a = "and you break free from the chains"
hold_on = Song([x, y, z, a], 4)
# From happy_bday, get the sing_me_a_song method and call it with parameter self
happy_bday.sing_me_a_song()
# From bulls_on_parade, get the sing_me_a_song method and call it with parameter self
bulls_on_parade.sing_me_a_song()
print()
matt_test.sing_me_a_song()
print("Rating for song: ", matt_test.rating)    # From matt_test, get the rating attribute
print(type(matt_test))
hold_on.sing_me_a_song()
