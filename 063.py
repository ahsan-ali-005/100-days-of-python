# Build mini note-taking app (file-based)

import os

filename = "note-taking-app.txt"

# File check: Agar file nahi hai to bana lo
if not os.path.exists(filename):
    with open(filename, "w") as f:
        pass

while True:
    print("\n--- NOTE TAKING APP ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Edit Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter Your Note: ")
        with open(filename, "a") as f:
            f.write(f"{note}\n")
        print("✅ Note Added!")

    elif choice == "2":
        with open(filename, "r") as f:
            notes = f.readlines()
        
        if not notes:
            print("📭 No Notes Currently...")
        else:
            print("\nYour Notes:")
            for i, n in enumerate(notes, 1):
                print(f"{i}. {n.strip()}")

    elif choice == "3":
        with open(filename, "r") as f:
            notes = f.readlines()
        
        if not notes:
            print("No notes to edit.")
            continue

        for i, n in enumerate(notes, 1):
            print(f"{i}. {n.strip()}")
            
        try:
            index = int(input("Enter note number to edit: ")) - 1
            if 0 <= index < len(notes):
                new_note = input("Enter new content: ")
                notes[index] = new_note + "\n"
                with open(filename, "w") as f:
                    f.writelines(notes)
                print("📝 Edited Successfully!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        with open(filename, "r") as f:
            notes = f.readlines()

        if not notes:
            print("No notes to delete.")
            continue

        for i, n in enumerate(notes, 1):
            print(f"{i}. {n.strip()}")

        try:
            index = int(input("Enter note number to delete: ")) - 1
            if 0 <= index < len(notes):
                notes.pop(index)
                with open(filename, "w") as f:
                    f.writelines(notes)
                print("🗑️ Deleted Successfully!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid Choice!")