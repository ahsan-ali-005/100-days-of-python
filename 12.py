# Find factorial (loop + recursion)

def fact(n):

    if n==1 or n==0:
        return 1

    return n*fact(n-1)


n=int(input("Enter a Number:"))

print("The factorial is: ",fact(n))


# with loop

n=int(input("Enter a Number:"))

fact=1

for i in range(1,n+1):

    fact=fact*i

print(fact)

