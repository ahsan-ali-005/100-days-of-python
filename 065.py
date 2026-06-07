# Build basic password manager (file encrypted text)

import os,json

filename = "password-manager.json"

# 1. Load Data from File (Logic)
if os.path.exists(filename):
    with open(filename, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            # Agar file khali ho ya kharab ho to default data load karein
            data=[]
else:
    # Pehli bar chalne par default data
    data=[]

def save_data():

    with open(filename,"w") as f:
        json.dump(data,f,indent=4)


def pass_encryption(password):

    return password[::-1]

def pass_decryption(password):

    return password[::-1]




while True:
    print("\n--- Welcome to Password Manager ---")
    print("1. Add New Password")
    print("2. View Saved Passwords")
    print("3. Update Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        website=input("Enter Website Name: ")
        username=input("Enter Username: ")
        password=input("Enter Password: ")

        encrypted_password=pass_encryption(password)
        new_entry={
            "website": website,
            "username": username,
            "password": encrypted_password
        }

        data.append(new_entry)
        save_data()
        print("Password Saved Successfully!")

    elif choice=="2":
        if not data:
            print("No passwords Saved!")
        
        else:
            for index, item in enumerate(data,1):
                print(f"{index}. {item["website"]} - {item["username"]} - {pass_decryption(item["password"])}")
    
    elif choice=="3":
        website=input("Enter Website to Update Password: ")

        found=False
        
        for item in data:
            if website==item["website"]:
                up_password=input("Enter New Password: ")

                item["password"]=pass_encryption(up_password)
                save_data()
                print("Password Updated Successfully!")
                found=True
                break
        if not found:
            print("This website is not present")

    elif choice=="4":
        website=input("Enter Website to Delete its Password: ")


        found=False

        for item in data:
            if website==item["website"]:
                data.remove(item)
                save_data()
                print("Password Deleted Successfully!")
                found=True
                break

        if not found:
            print("No such website!")

    elif choice=="5":
        print("GoodBye!")
        break

    else:
        print("Wrong Choice!")