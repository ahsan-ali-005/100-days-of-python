# Build mini diary app

import os
from datetime import datetime

filename="diaryapp.txt"

if not os.path.exists(filename):
    with open(filename,"w") as f:
        pass


while True:
    print("\n--- Diary APP ---")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Delete Entry")
    print("4. Update Entry")
    print("5. Exit")

    choice = input("Enter your choice: ")
    time = datetime.now()

    if choice == "1":

        entry=input("Enter Entry/Note to Add: ")

        with open(filename,"a") as f:

            f.write(f"{time} : {entry}\n")

        print("Entry Added Successfully!")

    elif choice == "2":

        with open(filename, "r") as f:

            content = f.readlines()

        if not content:
            print("No Entry Right Now!")
        
        else:
            for i,line in enumerate(content, 1):
                print(f"{i}. {line}")

        
    elif choice == "3":

        if not os.path.exists(filename):
            print("No diary found!")
            continue

        with open(filename, "r") as f:
            content = f.readlines()

        if not content:
            print("No Entry Right Now!")
            continue

        # Show entries
        for i, line in enumerate(content, 1):
            print(f"{i}. {line.strip()}")

        try:
            index = int(input("Enter line Number to Delete: ")) - 1

            if index < 0 or index >= len(content):
                print("Invalid index!")
                continue

            content.pop(index)

            with open(filename, "w") as f:
                f.writelines(content)

            print("Entry deleted successfully!")

        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        if not os.path.exists(filename):
            print("No diary found!")
            continue

        with open(filename, "r") as f:
            content = f.readlines()

        if not content:
            print("No Entry Right Now!")
            continue

        # Show entries
        for i, line in enumerate(content, 1):
            print(f"{i}. {line.strip()}")

        try:
            index = int(input("Enter line Number to Update: ")) - 1
            if index < 0 or index >= len(content):
                print("Invalid index!")
                continue

            new_entry=input("Enter New Entry: ")

            content[index] = f"{time} : {new_entry}\n"

            with open(filename, "w") as f:
                f.writelines(content)

            print("Entry Updated successfully!")

        except ValueError:
            print("Please enter a valid number!")
    

    elif choice == "5":
        break

    else:
        print("Invalid Choice!")

            




        