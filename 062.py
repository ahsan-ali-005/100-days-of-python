# Create JSON reader/writer

import json

data = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

with open("data.json", "w") as f:
    json.dump(data, f)

print("Data successfully written to JSON file!\n")

with open("data.json", "r") as f:
    loaded_data = json.load(f)

print("Data read from JSON file:")
print(loaded_data)
print("Name:", loaded_data["name"])