# Generate random password

import random

l_letter = "abcdefghijklmnopqrstuvwxyz"
u_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
char= "!@#$%^&*"

selector= l_letter + u_letter + num + char
length=int(input("Enter the length of password: "))
pas = ""

for i in range(1,length+1):
    a = random.choice(selector)
    pas=pas+a
print(pas)