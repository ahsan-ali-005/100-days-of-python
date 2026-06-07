# Log errors into file

# custom message logging
num1=int(input("Enter Number 1: "))
num2=int(input("Enter a Number 2: "))


if num2==0:
    with open("error-log.txt","a") as f:
        f.write("2nd Number must not be zero!\n")

else:
    div=num1/num2
    print(div)

# exception log to file
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except Exception as e:
    with open("error-log.txt", "a") as f:
        f.write(f"Error: {e}\n")