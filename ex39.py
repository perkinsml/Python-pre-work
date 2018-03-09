# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities by accessing the cities dictionary
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# Print some states by accessing the states dictionary
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Print the cities in a state by accessing the cities dictionary, using the state dictionary's value as a key
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# Print every state abbreviation
# Access the key-value pairs in the states dictionary as a list, referring to the items in each pair as state and abbrev
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abreviated {abbrev}")

# Print every city in state
print('-' * 10)
# Access the key-value pairs in the cities dictionary as a list, referring to the items in each pair as abbrev and city
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Now do both at the same time
# Use the abbrev in states to access the relevant city
# The inclusion of end = ' '  prints both statements on the same line
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}", end = ' ')
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# Safely get an abbreviation by state that might not be there
# Assign state to the value of the 'Texas' key in the states dictionary
state = states.get('Texas')
# If the state variable is empty, print a relevant statement
if not state:
    print("Sorry, no Texas")

# Get a city with a default value
# Assign city to the value of the 'TX' key in the cities dictionary.  If the key doesn't exist, assign the value to 'Does not exist'.
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")
