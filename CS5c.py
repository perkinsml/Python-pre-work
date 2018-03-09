
class Person(object):
    # Assign class variables shared across all instances of a class
    # In the last exampe, the friends list was shared across the instances.
    # We'll now give each instance it's own list be defining it as an instance variable
    age = 20
    gender = 'male'

    def __init__(self, friends = None):
        if friends is None:
            friends = []
        self.friends = friends

    # Define a method
    def print_stats(self):
        print(f"Age: {self.age}  Gender: {self.gender} Friends: {self.friends}")

# Create 2 instances of Person and assign them to linus and mampush
linus = Person()
mampush = Person()

#Assign a new attribute to the Linus instance only
linus.name = "Linus"
# Create an instance of Person passing a friends list to the __init__() and assign it to Jan
# Change the gender attribute for jan to 'female'
jan = Person(['Fred', 'Barney', 'Wilma'])
jan.gender = 'female'

# Print class attributes for each instance
print("Linus stats")
print(linus.name)
print(linus.age)
print(linus.gender)
print(linus.friends)
print()
print("Mampush stats")
print(mampush.age)
print(mampush.gender)
print(mampush.friends)
print()
print("Jan stats")
print(jan.age)
print(jan.gender)
print(jan.friends)
jan.print_stats()

print()
print("Adding friends for mampush")
mampush.friends.append('Petunia')
mampush.friends.append('Elmer')
# Adding to the list class attribute shares values across all instances, sinces lists are mutable
print(f"Mampush friends: {mampush.friends}")
print(f"Linus friends: {linus.friends}")
