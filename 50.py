# Create Contact Book (file storage)

class Contact_Book:
    def __init__(self):
        self.filename="contacts.txt"

    def add_contact(self):
        name=input("Enter Name: ")
        phone=input("Enter Phone: ")
        email=input("Enter Email: ")

        with open(self.filename, "a") as f:
            f.write(f"{name},{phone},{email}\n")

        print("Contact Added Successfully!")
    
    def search_contact(self):
        name=input("Enter Name of the person to search for the contact: ")

        with open(self.filename,"r") as f:
            lines=f.readlines()
            found=False
            for line in lines:
                if line.startswith(name):
                    print(f"Yes Contact with {name} is present..")
                    found=True
                    break
            if not found:
                print(f"No Contact present with {name}")

    
    def del_contact(self):
        name=input("Enter Name of the person to Delete its Contact: ")
        with open(self.filename,"r") as f:
            lines=f.readlines()
            found=False
            for line in lines:
                if line.startswith(name):
                    found=True
                    del line
                    print("Contact Deleted")
                    break

            if not found:
                print(f"No contact with {name}")

    def view_contact(self):
        name=input("Enter Name of the person to View its Contact: ")
        with open(self.filename,"r") as f:
            lines=f.readlines()
            found=False
            for line in lines:
                if line.startswith(name):
                    found=True
                    print(line)
                    break
            if not found:
                print(f"No contact with {name}")


t=Contact_Book()

while True:
    print("\n1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        t.add_contact()
    elif choice == "2":
        t.view_contact()
    elif choice == "3":
        t.search_contact()
    elif choice == "4":
        t.del_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")