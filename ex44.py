# An example of implicit inheritence, where functions are defined in the parent
# and not the child i.e. functions and variables in the base class (Parent)
# are automatically inherited by the subclass (Child).
# An example of an override explicitly, where a function is defined in the subclass
# with the same name as that in the base class, and called by an instance of the subclass (Child)
# An example of calling a function from the Base Class, where an override function has been
# defined in the subclass
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT alterered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()

dad = Parent()      # Set dad to an instance of class Parent
son = Child()       # Set son to an instance of class Child

dad.implicit()      # Accesses the implicit function defined in the Parent class
son.implicit()      # Accesses the implicit function defined in the Parent class, as an override hasn't been defined in the Child class

dad.override()      # Accesses the override function defined in the Parent class
son.override()      # Accesses the override function defined in the Child class, as an override has been defined in the subclass

dad.altered()       # Accesses the altered function defined in the Parent class
son.altered()       # Accesses the altered function defined in the Chile class, but then calls the altered method in the super (i.e. base) class
