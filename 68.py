# Playfair Encryption Program

data_list=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def setup_passkey(passkey):
    
    new_passkey=  passkey.replace(" ","").replace("j","i")
    l=[]
    for char in new_passkey:
        if char in l:
            continue
        else:
            l.append(char)

    for char in data_list:
        if char in l:
            continue
        else:
            l.append(char)

    return l

def make_matrix(l):

    matrix=[]
    row1=l[0:5]
    row2=l[5:10]
    row3=l[10:15]
    row4=l[15:20]
    row5=l[20:25]

    matrix=[row1,row2,row3,row4,row5]

    return matrix


def setup_plaintext(plain_text,filler_letter):

    new_text= plain_text.replace(" ", "").replace("j","i")
    i=0
    l=[]

    while i< len(new_text):
        if i == len(new_text)-1:
            pair_of_two= new_text[i] + filler_letter
            l.append(pair_of_two)
            i+=1

        elif new_text[i]==new_text[i+1]:
            pair_of_two= new_text[i] + filler_letter
            l.append(pair_of_two)
            i+=1
        else:
            pair_of_two= new_text[i] + new_text[i+1]
            l.append(pair_of_two)
            i += 2

    return l

def setup_ciphertext(cipher_text):
    
    new_text = cipher_text.replace(" ", "").replace("j", "i")
    pairs = []
    for i in range(0,len(new_text),2):
        pair = new_text[i:i+2]
        pairs.append(pair)

    return pairs

def find_position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def encrypt_text(matrix, pairs):
    result = ""

    for pair in pairs:
        a = pair[0]
        b = pair[1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same Row
        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        # Same Column
        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        # Rectangle
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result



def decrypt_text(matrix, pairs):
    
    result=""

    for pair in pairs:

        a = pair[0]
        b = pair[1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same Row
        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]

        # Same Column
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]

        # Rectangle
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result




while True:
    print("1==> Encrypt Text")
    print("2==> Decrypt Text")
    print("3==> Exit")


    choice=input("Enter Choice: ")

    if choice=="1":
        passkey=input("Enter Password Key: ").lower()

        complete_list = setup_passkey(passkey)
        matrix = make_matrix(complete_list)

        plain_text=input("Enter Plaintext: ").lower()
        filler_letter=input("Enter Filler Letter: ").lower()

        l_plaintext_pairs = setup_plaintext(plain_text,filler_letter)

        ciphertext=encrypt_text(matrix,l_plaintext_pairs)
        print(f"The Cipher text is: {ciphertext.upper()}")


    elif choice=="2":
        passkey=input("Enter Password Key: ").lower()
        complete_list = setup_passkey(passkey)
        matrix = make_matrix(complete_list)

        cipher_text=input("Enter Ciphertext: ").lower()
        filler_letter=input("Enter Filler Letter: ").lower()

        l_ciphertext_pairs = setup_ciphertext(cipher_text)

        plain_text=decrypt_text(matrix,l_ciphertext_pairs)
        print(f"The Plain text is: {plain_text.lower()}")
        

    elif choice=="3":
        print("Good Bye!")
        break

    else:
        print("Please Enter a Valid Choice!")