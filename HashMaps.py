# Initialising Dict or hashmap
state_visited = {}

states = ["New York", "New Jersey", "Kansas"]
# First insert Key
# Assign empty array everytime
state_visited["America"] = []
state_visited["America"].append(states)
state_visited["America"].append("Omaha")
print(state_visited)

# Default dict initialized empty array for elements to be added.

from collections import defaultdict
# Assigned array automatically for all keys
city_visited = defaultdict(list)

NYcities = ["NYC", "Bronx"]
NJcities = ["Princeton", "Jersey City"]
MOCities = ["Kansas City"]
city_visited["New York"] += NYcities
city_visited["New Jersey"].append(NJcities)
city_visited["Kansas"].append(MOCities)

print(city_visited)

# Extracting values

print(city_visited.keys())
print(city_visited.values())
print(city_visited.items())
