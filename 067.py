# Create student result storage system

import os, json

filename = "student_system.json"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        json.dump([], f)

with open(filename, "r") as f:
    try:
        students = json.load(f)
    except json.JSONDecodeError:
        students = []


def save_data():
    with open(filename,"w") as f:
        json.dump(students,f,indent=4)

    
while True:

    print("\n--- Welcome to Student Management System ---")
    print("1. Add New Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Check Student Total & Percentage & Grade")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice=="1":
        id=input("Enter Student ID: ")
        name=input("Enter Student Name: ")
        no_subjects=int(input("Enter Student Number of Subjects: "))
        marks_dic={}
        for index in range(1,no_subjects+1):
            marks=int(input(f"Enter marks of Subject {index}: "))

            marks_dic[index]=marks

        students.append({"id":id, "name": name, "marks": marks_dic})
        save_data()
        print("Student Successfully added!")

    elif choice=="2":
        id=input("Enter ID of the Student: ")

        found=False
        for items in students:
            if items["id"]==id:
                print(f"ID: {items['id']}")
                print(f"Name: {items['name']}")
            
                print("Marks:")
                for num, marks in items["marks"].items():
                    print(f"  {num} : {marks}")

                found=True
                break

        if not found:
            print("No Student is present with this id.")

    elif choice=="3":
        id=input("Enter ID of the Student to update: ")
        i=1
        found=False
        for items in students:
            
            if items["id"]==id:
                for key in items["marks"]:
                    new_marks = int(input(f"Enter new marks of Subject {key}: "))
                    items["marks"][key] = new_marks

                print("Marks Updated!")
                save_data()
                found=True
                break
        
        if not found:
            print("No Student is present with this id.")

    elif choice=="4":
        id=input("Enter ID of the Student to Check Student Total & Average: ")
        i=0
        total=0
        found=False
        for items in students:
            if items["id"]==id:

                for key,value in items["marks"].items():
                    i+=1
                    total+=value

                average=total/i

                print(f"Total is: {total}")
                print(f"Average is: {average}")

                found=True
                break

        if not found:
            print("No Student is present with this id.")


    elif choice=="5":
        id=input("Enter ID of the Student to Delete: ")
        found=False

        for items in students:
            if items["id"]==id:
                students.remove(items)
                print("Deleted Successfully!")
                save_data()
                found= True
                break

        if not found:
            print("No Student is present with this id.")

    elif choice=="6":
        print("Good Bye!")
        break

    else:
        print("Invalid Choice!")

