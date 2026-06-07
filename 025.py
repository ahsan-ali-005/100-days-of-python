# Find frequency of characters using dict

char=list(input("Enter String: "))
d={}

for i in char:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)

