# Rotate list k times (left/right)

l=[0,1,2,3,4,5,6,7,8]

k=int(input("Enter Value of K: "))
n=len(l)
k= k % n

print("1. Left Rotation: ")
print("2. Right Rotation: ")

choice=input("Enter your choice: ")


if choice=="1":
    new_list=l[k:]+l[:k]
    print(new_list)

elif choice =="2":
    new_list=l[-k:]+l[:-k]
    print(new_list)

else:
    print("Please Enter a Valid choice.")