# Code


# Notice that:
# locations is a dictionary of dictionaries
# North America (Continent) is a dictionary
# USA (Country) is a key
# ['Mountain View'] (City) is a list acting as a value.
# A new City within USA Country can be "appended" to the given list.

# TODO: Print a list of all cities in the USA in alphabetic order.

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country


# Task 1: You need to add the cities below by modifying the given structure. Cities to add:
# Bangalore ( India, Asia )
# New Delhi ( India, Asia )
# Atlanta ( USA, North America )
# Cairo ( Egypt, Africa )
# Shanghai ( China, Asia )

# Be careful, while adding a city in an existing country. Consider adding it to the existing list of cities as:
# TODO: locations['Asia']['India'].append('New Delhi')


# Task 1 - Solution
locations = {'North America': {'USA': (['Mountain View'])}}
locations['North America']['USA'].append('Atlanta')

locations['Asia'] = {'China': ['Shanghai']}
locations['Asia'] = {'India': 'Bangalore'}

locations['Asia']['India'].append('New Delhi')

locations['Africa'] = {'Egypt': ['Cairo']}


print(locations)

# Task 2 - Solution
# Part 1 - A list of all cities in the USA in alphabetic order.

print(1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)

# Part 2 - List all cities in Asia, in alphabetic order.
print(2)
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append('{} - {}'.format(city, country))

asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print(city)
