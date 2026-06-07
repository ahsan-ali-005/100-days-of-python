# Find all non-repeating character

string="abbccdddefff"

freq={}


for ch in string:

    freq[ch]=freq.get(ch,0)+1

for ch in freq:
    if freq[ch]==1:
        print(f"{ch} is non repeating.")