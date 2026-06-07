# Remove Duplicates from a List (Without Using set)

l=[1,2,3,3,4,4,2,"harry","berry","larry","berry"]
new_l=[]

for i in l:
    if i not in new_l:
        new_l.append(i)

print(new_l)