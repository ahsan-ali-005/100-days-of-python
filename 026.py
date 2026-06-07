# Find duplicate values in list

l=[1,2,2,3,4,5,1]
l2=[]
l3=[]

for i in l:
    if i not in l2:
        l2.append(i)
    else:
        if i not in l3:
            l3.append(i)

print(l3)
        