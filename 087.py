# secret language code.

import random, string

def encode(text):
    if len(text)<3 and not len(text)==0:
        text=text[::-1]
        return text
    
    else:
        i=0
        text=text[1:]+text[0]
        s_char = "".join(random.choices(string.ascii_letters, k=3)).lower()
        l_char = "".join(random.choices(string.ascii_letters, k=3)).lower()
        encoded_text= s_char+text+l_char
        return encoded_text


def decode(text):
    # case 1: length < 3
    if len(text) < 3 and len(text) != 0:
        return text[::-1]
    
    # case 2: length >= 3
    else:
        # remove 3 chars from start and end
        text = text[3:-3]
        
        # bring last char to front
        text = text[-1] + text[:-1]
        
        return text


while True:
    print("1. Encode the text")
    print("2. Decode the text")
    print("3. Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        text=input("Enter text to Encode: ")
        encoded=encode(text)
        print(f"Encoded text is: {encoded}")

    elif choice=="2":
        text=input("Enter text to Decode: ")
        decoded=decode(text)
        print(f"Decoded text is: {decoded}")
    elif choice=="3":
        print("Goodby!")
        break

    else:
        print("Invalid Choice!")