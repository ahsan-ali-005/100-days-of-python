# Find missing number in list (1 to n)

l = [0,1,2,3,4,6,8,9,12,33]
s = set(l)

for i in range(min(l), max(l) + 1):
    if i not in s:
        print(f"{i} is missing.")