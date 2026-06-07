# Generate multiplication table

try:
    n=int(input("Enter a Number:"))

    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

except ValueError as e:
    print(e)