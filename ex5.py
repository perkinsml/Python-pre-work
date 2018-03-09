name = "Zed. A. Shaw"
age = 35             # Not a lie
height = 74          # Inches
weight = 180         # Pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Convert height and weight to metric values
inches_to_cms_conv = 2.54
pounds_to_kgs_conv = 0.453592
height_in_cms = height * inches_to_cms_conv
weight_in_kgs = weight * pounds_to_kgs_conv
print(f"Let's talk about {name} .")
print(f"He's {height_in_cms} cms tall.")
print(f"He's {weight_in_kgs} kgs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"He's teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height_in_cms + weight_in_kgs
print(f"If I add {age}, {height_in_cms}, and {weight_in_kgs} I get {total}.")

# I can round floating point numbers using the round function.  Below I round to 2 decimal places.
print(f"If I add {age}, {round(height_in_cms,2)}, and {round(weight_in_kgs,2)} I get {round(total,2)}.")

# I can round floating point numbers using the round function.  Below I round to 2 decimal places.
print(f"He's combined weight and height is {weight_in_kgs + height_in_cms} - which is ridiculous sum to do!")

# Testing the placement of a comma and includsion of a boolean in the f string
print(f"The numerical value of {name}'s height is greater than his weight? {height_in_cms > weight_in_kgs}.")
