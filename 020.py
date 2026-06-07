# Find longest word in string

s = "This is a stirng and this is very short"
words= s.split()
longest=""

for i in words:
    if len(i)>len(longest):
        longest=i

print(longest)