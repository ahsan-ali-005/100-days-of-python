# find all repeating characters

string="abbccdddefff"
freq={}

for ch in string:
    freq[ch]=freq.get(ch,0)+1

for ch in freq:
    if freq[ch]>1:
        print(f"{ch} is repeating.")