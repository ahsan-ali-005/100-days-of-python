# Build a simple calculator with all 4 operations using try-except

def get_numbers():
    while True:
        try:
            num1=int(input("Enter 1st Number: "))
            num2=int(input("Enter 2nd Number: "))
            return num1, num2
        except ValueError:
            print("Please Enter Valid Integers!")
    
while True:
    print("1=> Addition")
    print("2=> Subtraction")
    print("3=> Multiplication")
    print("4=> Division")
    print("5=> Exit")

    op= input("Enter your Choice: ")

    if op=="1":
        a,b= get_numbers()
        s=a+b
        print(f"Sum is : {s}\n")
    elif op=="2":
        a,b = get_numbers()
        sub = a-b
        print(f"Subtraction is : {sub}\n")
    elif op=="3":
        a,b = get_numbers()
        mul = a*b
        print(f"Product is : {mul}\n")
    elif op=="4":
        a,b = get_numbers()
        if b==0:
            print(" Can't divide by zero!\n")
        else:
            div = a/b
            print(f"Division is : {div}\n")
    elif op=="5":
        print("Exiting...")
        break
    else:
        print("Invalid Choice!\n")