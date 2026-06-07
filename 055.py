# Count most common word in file

d={}

with open("new.txt", "r") as f:

    a=f.read().lower()
    words=a.split()

    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word]=1

    max_frequency=0
    most_frequent_word=""

    for i in d:
        value= d[i]
        if max_frequency<value:
            max_frequency=value
            most_frequent_word=i
    
    print(f"Most common word is: {most_frequent_word}: {max_frequency}")

