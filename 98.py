# Remove duplicates from a list while preserving order

l=[1,2,3,4,2,3,4,6,5,7,8,6]

l2=[]

for item in l:
    if item not in l2:
        l2.append(item)
    else:
        continue

print(l2)