
class Person(object):
    # Assign class variables shared across all instances of a class
    # Note, the values are shared for mutable variable types
    age = 20
    gender = 'male'
    friends = []

    def __init__(self):
        pass

    # Define a method
    def print_stats(self):
        print(f"Age: {self.age}  Gender: {self.gender} Friends: {self.friends}")

# Create 2 instances of Person and assign them to linus and mampush
linus = Person()
mampush = Person()

# Print class attributes for each instance
print("Linus stats")
print(linus.age)
print(linus.gender)
print(linus.friends)

print("Mampush stats")
print(mampush.age)
print(mampush.gender)
print(mampush.friends)

print()
print("Adding friends for mampush")
mampush.friends.append('Petunia')
mampush.friends.append('Elmer')
# Adding to the list class attribute shares values across all instances, sinces lists are mutable
print(f"Mampush friends: {mampush.friends}")
print(f"Linus friends: {linus.friends}")

# Change age of Mampush
print("Changing age of Mampush.")
# The code below doesn't change the age of Linus as age is an int, which is immutable
mampush.age = 25
print(f"Mampush age: {mampush.age}")
print(f"Linus age: {linus.age}")

print()
print()
print("Now we'll use the class method to print")
linus.print_stats()
mampush.print_stats()
