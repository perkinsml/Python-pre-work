# Welcome to Matt's Python Cheat Sheet, covering
# Classes

class Shape(object):

    colour = "blue"

    def __init__(self, x, y):               # The function called __init__ is run when we create an instance of Shape
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area(self):
        return self.x * self.y              # Self is the first parameter in any function defined inside a class

    def perimeter(self):                    # Self is the first parameter in any function defined inside a class
        return 2 * self.x + 2 * self.y

    def describe(self, text):               # Self is the first parameter in any function defined inside a class
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

rectangle = Shape(100, 45)
print("Area of rectangle is: ", rectangle.area())
print("Perimeter of rectangle is: ", rectangle.perimeter())
rectangle.describe("A rectangle has 4 sides, 2 of which are double the size of the other two!")
print(rectangle.description)
print("Making the rectangle 50% smaller... ")
rectangle.scaleSize(0.5)
print("The new area is: ", rectangle.area())
print(f"The colour of the rectangle is {rectangle.colour} .")

print()
print('-' * 50)
print("INHERITANCE!")
print()
# Python makes inheritance really easy. We define a new class, based on another, 'parent' class.
# Our new class brings everything over from the parent, and we can also add other things to it.
# If any new attributes or methods have the same name as an attribute or method in our parent class,
# it is used instead of the parent one.

class Square(Shape):                # Define a new class Square, that inherits from Shape
# This lets us describe a square really quickly. That's because we inherited everything from the shape class,
# and changed only what needed to be changed. In this case we redefined the __init__ function of Shape so that
# the X and Y values are the same.
    colour = "red"

    def __init__(self,x):
        self.x = x
        self.y = x

my_square = Square(10)
print("Area of my square is: ", my_square.area())
print("Perimeter of my square is: ", my_square.perimeter())
my_square.describe("A square has 4 equal sides.")
print(my_square.description)
print("Making the square 50% smaller... ")
my_square.scaleSize(0.5)
print("The new area is: ", my_square.area())
print(f"The colour of the square is {my_square.colour} .")

class Circle(Shape):

    def __init__(self,x):
        self.x = x

    def area(self):
        return 3.14 * self.x * self.x

    def perimeter(self):
        return 3.14 * self.x * 2

    def scaleSize(self, scale):
        self.x = self.x * scale

my_circle = Circle(100)
print("Area of my circle is: ", my_circle.area())
print("Perimeter of my circle is: ", my_circle.perimeter())
my_circle.describe("A circle has 0 sides!")
print(my_circle.description)
print("Making the circle 50% smaller... ")
my_circle.scaleSize(0.5)
print("The new area is: ", my_circle.area())
print(f"The colour of the circle is {my_circle.colour} .")
