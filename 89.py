# Rail Fence Technique

def encrypt():
    text = input("Enter text: ").replace(" ", "")
    depth = int(input("Enter depth: "))
    
    rails = [[" " for _ in range(len(text))] for _ in range(depth)]
    
    row, direction = 0, 1
    
    for col in range(len(text)):
        rails[row][col] = text[col]
        
        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1
            
        row += direction
    
    cipher = ""
    for r in rails:
        for ch in r:
            if ch != " ":
                cipher += ch
    
    print("Encrypted:", cipher)

def decrypt():
    text = input("Enter text: ").replace(" ", "")
    depth = int(input("Enter depth: "))

    # step 1: empty grid
    rails = [[" " for _ in range(len(text))] for _ in range(depth)]

    # step 2: mark zig-zag path with '*'
    row, direction = 0, 1
    for col in range(len(text)):
        rails[row][col] = "*"

        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1

        row += direction

    # step 3: fill characters row-wise
    index = 0
    for i in range(depth):
        for j in range(len(text)):
            if rails[i][j] == "*" and index < len(text):
                rails[i][j] = text[index]
                index += 1

    # step 4: read zig-zag
    result = ""
    row, direction = 0, 1
    for col in range(len(text)):
        result += rails[row][col]

        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1

        row += direction

    print("Decrypted:", result)


while True:
    print(f"{"*"*10} Rail Fence Technique {"*"*10}")
    print("1==> Encrypt")
    print("2==> Decrypt")
    print("3==> Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        encrypt()

    elif choice=="2":
        decrypt()

    elif choice=="3":
        print("Bye!")
        break

    else:
        print("Enter a Valid choice.")