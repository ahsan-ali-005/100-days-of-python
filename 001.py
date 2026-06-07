# Reverse a string (without slicing)
a = "This is a string"
reverse_a = ""

for char in a:
    reverse_a = char + reverse_a
    
print(reverse_a)