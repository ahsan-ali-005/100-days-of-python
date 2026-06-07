# Shift Cipher encryption/decryption program

data={
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,
    "G":6,
    "H":7,
    "I":8,
    "J":9,
    "K":10,
    "L":11,
    "M":12,
    "N":13,
    "O":14,
    "P":15,
    "Q":16,
    "R":17,
    "S":18,
    "T":19,
    "U":20,
    "V":21,
    "W":22,
    "X":23,
    "Y":24,
    "Z":25
}


while True:
    print("1==> Encrypt Text")
    print("2==> Decrypt Text")
    print("3==> Exit")


    choice=input("Enter Choice: ")

    if choice=="1":
        plain_text=input("Enter Text to Encrypt: ").upper()
        key_value=int(input("Enter Key Value: "))
        cipher_text=""
        for char in plain_text:
            plain_text_value = data[char]
            cipher_value=(plain_text_value + key_value) % 26

            for key, value in data.items():

                if value == cipher_value:

                    cipher_text+=key

        print(f"The Cipertext for {plain_text.lower()} is: {cipher_text}\n")

    elif choice=="2":
        cipher_text=input("Enter Text to Decrypt: ").upper()
        key_value=int(input("Enter Key Value: "))
        plain_text=""

        for char in cipher_text:
            cipher_text_value = data[char]
            plain_value=(cipher_text_value - key_value) % 26

            for key,value in data.items():
                if value==plain_value:

                    plain_text+=key

        print(f"The Plaintext for {cipher_text} is: {plain_text.lower()}\n")

    elif choice=="3":
        print("Good Bye!")
        break

    else:
        print("Please Enter a Valid Choice.")
