# Count frequency of elements in list

l=[1,2,3,4,5,5,5,2,1]
d={}

for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)