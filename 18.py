# Find common elements in two lists

l1=[1,2,3,4,"Ahsan","Ali"]
l2=[0,2,5,4,"Harry","Ali"]

l=[]

for i in l1:
    if i in l2:
        l.append(i)
print(f"The common elements are: {l}")