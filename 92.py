# FizzBuzz (1-100): print Fizz/Buzz/Fizz/Buzz (FizzBuzz logic)
try:
    r = int(input("Enter range (1-100): "))
except ValueError:
    print("Please enter a valid integer!")
else:
    for i in range(1, r + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)