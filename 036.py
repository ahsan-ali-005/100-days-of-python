# Find most frequent word in text

txt="my name is Ahsan Ali and Ahsan Ali is very good and Ahsan Ali is very bad and Ahsan Ali is Ahsan Ali Ali" 
a= txt.split()

dic={}

for i in a:
    if i not in dic:
        dic[i]=1
    elif i in dic:
        dic[i]+=1

max_frequency=0
most_frequency_word=""
for i in dic:

    a=dic.get(i)

    if a>max_frequency:
        max_frequency=a
        most_frequency_word=i

print(most_frequency_word)
    
    
    