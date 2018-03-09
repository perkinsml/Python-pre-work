# Welcome to Matt's Python Cheat Sheet, covering
# dictionaries

a_dict={'Name': 'Matt', 'Age': 43, 'Height': 5 * 12 + 11, 45: 'Street Number'}

print(type(a_dict))

print(a_dict['Name'])
print(a_dict['Age'])
print(a_dict['Height'])
print(a_dict[45])
print(a_dict)
a_dict['Weight'] = 85       # Add this key-value pair to a_dict
print(a_dict)
print(f"Matt's height is {a_dict['Height']}")

print()
print(a_dict)
print(a_dict.keys())
print(a_dict.values())
print(a_dict.items())
print(list(a_dict.items())) # Print the key-value pairs within a_dict as tuples

for x, y in list(a_dict.items()):
    print(f"{x}: {y}")

print()

song = a_dict.get('Song')
print(song)
print(type(song))

if not song:
    print("Song doesn't exist")

movie = a_dict.get('Movie', 'Movie doesn\'t exist')
print(movie)
