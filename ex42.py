# Animal is-a object
class Animal(object):

    def make_noise(self):
        print("Something inaudble")

# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

    def make_noise(self):
        print("Woof, Woof")

# Cat is a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

    def make_noise(self):
        print("Meoooooow")

# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet
        self.pet = None

    def make_noise(self):
        print("Natter, natter")

# Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee inherits name from the Person
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

    def make_noise(self):
        print("Moan, moan")

# Fish is-a object
class Fish(object):
    pass

# Salmon is a Fish
class Salmon(Fish):
    pass

# Halibut is a Fish
class Halibut(Fish):
    pass


# rover is-a dog
rover = Dog("Rover")
print(rover.name)
rover.make_noise()

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")
print(mary.name)
print(mary.pet)

# mary has-a satan
mary.pet = satan
print(mary.pet.name)

# frank is-a Employee. frank has-a name "Frank" has-a salary 120000
frank = Employee("Frank", 120000)
print(frank.name)
print(frank.salary)
print(frank.pet)
frank.make_noise()
super(Employee, frank).make_noise()
# frank has-a rover
frank.pet = rover
print(frank.pet.name)

# flipper is-a Fish
flipper = Fish()
print(type(flipper))

# crouse is a Salmon
crouse = Salmon()

# harry is a Halibut
harry = Halibut()
