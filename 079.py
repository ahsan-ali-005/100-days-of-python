# Find first non-repeating character

string = "aabccddedff"

for ch in string:
    if string.count(ch) == 1:
        print(ch)
        break


# Method 2

string = "aabccddedff"

freq = {}

for ch in string:
    freq[ch] = freq.get(ch, 0) + 1

for ch in string:
    if freq[ch] == 1:
        print(ch)
        break


