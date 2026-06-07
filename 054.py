# Count lines in file

with open("contacts.txt", "r") as f:

    a= f.readlines()
    count=0
    for line in a:
        count+=1
    print(count)