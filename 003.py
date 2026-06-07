# Check palindrome (string + number)

n=input("Enter String or Numbers: ")
reversed_n= n[::-1]

if n==reversed_n:
    print(f"The input is palindrome: {n}")
else:
    print("The input is not a palidrome.")