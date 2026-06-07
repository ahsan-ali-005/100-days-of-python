# Flatten nested list (1 level only)

l1=[3,4,"Harry","Larry"]
l2=[1,2,3,4,"Ahsan","Ali", l1]

flat=[]

for i in l2:
    if type(i)==list:
        for j in i:
            flat.append(j)
    else:
        flat.append(i)

print(flat)