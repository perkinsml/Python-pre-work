# Welcome to Matt's Python Cheat Sheet, covering
# Classes

class Person(object):
    pass

class Employee(Person):

    def __init__(self, status):
        self.status = status

        if self.status == 'ft':
            self.salary = 2000
            self.max_hours = 60
        elif self.status == 'pt':
            self.salary = 1500
            self.max_hours = 30
        else:
            print("Employee type not recognised.")
            self.salary = None
            self.max_hours = None

    def rating(self, code):
        if code == 1:
            return "Exceeds"
        elif code == 2:
            return "Meets"
        else:
            return "Sacked"


mary = Employee('ft')
john = Employee('pt')
ed = Employee('unemployed')

print(f"Mary's salary is: ${mary.salary} and her maximum hours are {mary.max_hours}.")
print(f"John's salary is: ${john.salary} and his maximum hours are {john.max_hours}.")
print(f"Ed's salary is: ${ed.salary} and his maximum hours are {ed.max_hours}.")

print(f"Mary's performance rating is {mary.rating(2)}.")
print(f"John's performance rating is {john.rating(1)}.")
print(f"Ed's performance rating is {mary.rating(3)}.")
