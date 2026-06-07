# Convert binary to decimal

def binary_to_deci(num,power,decimal):

    for i in num[::-1]:

        decimal+= int(i)*2**power
        power+=1

    return decimal


decimal=0
power=0
num=input("Enter Binary Number: ")

result=binary_to_deci(num,power,decimal)
print(f"The Number in decimal is: {result}")


