# Find max and min manually

n1=int(input("Enter Number:"))
n2=int(input("Enter Number:"))
n3=int(input("Enter Number:"))


if n1>=n2 and n1>=n3:
    print(f"The Max number is {n1}")

elif n2>=n1 and n2>=n3:
    print(f"The Max number is {n2}")

else:
    print(f"The Max number is {n3}")


if n1<=n2 and n1<=n3:
    print(f"The Min number is {n1}")
elif n2<=n1 and n2<=n3:
    print(f"The Min number is {n2}")
else:
    print(f"The Min number is {n3}")