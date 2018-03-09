# Welcome to Matt's Python Cheat Sheet, covering
# if, for and while loops (including infinite while loops
# and try and except).
# This also includes an exit and a try-except

from sys import exit

x = 4
y = ""
if x:
    print("This runs, as x has content")

if y:
    print("This won't run, as y is empty")

a = 4
b = 5
c = 6
if a > b:
    print("a is greater than b")
elif b > c:
    print("b is greater than c")
else:
    print("c is the largest number")

fruits = ['apples', 'oranges', 'pears', 'apricots']
for fruit in fruits:
    print(f"The fruit is {fruit}.")

a_list = []
for i in range(0, 50, 10):
    a_list.append(i)
    print(i)

b_list = list(range(0, 50, 10))
print(b_list)

i = 0
numbers = []
while i < 10:
    numbers.append(i)
    i = i + 2
print(numbers)

number_test = input("Enter a number: ")
try:
    print("Your number is: ", int(number_test))
except:
    print("You provided non-numeric input.")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That wasn't a valid number.  Try again...")

def exit_function():
    exit(0)

while True:
    print("Enter a letter: a, b or c.")
    letter = input("> ")
    if letter in "abc":
        print("You chose an appropriate letter!  Your job is done!")
        exit_function()
