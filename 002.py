# Count vowels in a string

s="This is a string.".lower()
vowel=0
for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o"  or char == "u":
        vowel+=1

print(vowel)