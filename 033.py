#Sort list of dictionaries by key

data = [
    {"name": "Ahsan", "age": 25},
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 28}
]


sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)
