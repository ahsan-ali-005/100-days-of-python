# Find all substrings of string

# ABC     

string=input("Enter a String to find its Substrings: ")
length=len(string)

for i in range(length):
    for j in range(i+1,length + 1):
        print(string[i:j])