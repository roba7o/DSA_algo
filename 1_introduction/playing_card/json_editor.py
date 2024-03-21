import json
import random

# Load the list of names from the JSON file
with open('names.json', 'r') as file:
    names = json.load(file)

# Generate a random number between 1000 and 100000 and append it to each name
result = [{name: random.randint(1000, 100000)} for name in names]

# Write the result back to a JSON file
with open('names_with_numbers.json', 'w') as file:
    json.dump(result, file, indent=4)
