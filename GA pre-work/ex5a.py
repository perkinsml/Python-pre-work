# checks whether a four-digit year is a leap year in the Gregorian calendar.
# In the Gregorian calendar, three criteria must be taken into account to identify leap years::
# 1) If the year can be evenly divided by 400, it is a leap year.
# 2) If the year can be divided by 100 and not 400, it is not a leap year.
# 3) If the year can be divided by 4 but not by 100, it is a leap year.

def is_leap(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0 and n % 400 != 0:
        return False
    elif n % 4 == 0 and n % 100 !=0:
        return True
    else:
        return False

# TESTING
#print(is_leap(2000))
#print(is_leap(1600))
#print(is_leap(2001))

#print(is_leap(1900))
#print(is_leap(1800))
#print(is_leap(1700))

#print(is_leap(1996))
#print(is_leap(1995))
#print(is_leap(1992))


# Define the function calc_default_add(), which — when given two numeric
# inputs and the string "add" or "sub" — either adds or subtracts the two
# numbers appropriately. If the string is not provided as a third parameter,
# make the default operation add().  Also make sure that, if any other operation
# is provided as the third parameter, you print the string "Valid operations: add, sub".

def calc_default_add(x, y, op="add"):
    if op == "add":
        return x + y
    elif op == "sub":
        return x - y
    else:
        return "Valid operations: add, sub."

# TESTING
#print(calc_default_add(5, 9))
#print(calc_default_add(5, 11, "add"))
#print(calc_default_add(5, 11, "sub"))
#print(calc_default_add(5, 11, "div"))
