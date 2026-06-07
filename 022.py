# Create calculator using functions

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        return b/a
    else:
        return a/b



n1=int(input("Enter Number one: "))
n2=int(input("Enter Number two: "))

op=input("Enter Operation(+,-,*,/): ")

if op=="+":
    print("The Sum is:", add(n1,n2))
elif op=="-":
    print("The Subtract is:", sub(n1,n2))
elif op=="*":
    print("The Product is:", mul(n1,n2))
elif op=="/":
    print("The Division is:", div(n1,n2))
else:
    print("Invalid Operation!")

