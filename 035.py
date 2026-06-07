# Count uppercase/lowercase letters

string=input("Enter a String: ")
uppercount=0
lowercount=0

for i in string:
    
    if i.isupper():
        uppercount+=1
    elif i.islower():
        lowercount+=1

print(f"The uppercase count is: {uppercount} and lowercase is {lowercount}")