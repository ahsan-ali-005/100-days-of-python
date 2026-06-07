# Find second largest number in list

l=[2,4,6,7,8,9,7,6,13,10,12]
 
largest=l[0]
second_largest=l[0]

for i in l:
    if i>largest:
        second_largest= largest
        largest=i
   
    elif i > second_largest and i != largest:
        second_largest = i


print(second_largest)