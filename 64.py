# Create simple expense tracker

import os
import json

filename = "expense-tracker.json"

if os.path.exists(filename):
    with open(filename, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = [
                {"id": 1, "amount": 0, "category": "Food"},
                {"id": 2, "amount": 0, "category": "Travel"},
                {"id": 3, "amount": 0, "category": "Bills"},
                {"id": 4, "amount": 0, "category": "Shopping"}
            ]
else:
    data = [
        {"id": 1, "amount": 0, "category": "Food"},
        {"id": 2, "amount": 0, "category": "Travel"},
        {"id": 3, "amount": 0, "category": "Bills"},
        {"id": 4, "amount": 0, "category": "Shopping"}
    ]

def save_data():
    """Function to save current data to JSON file"""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def show_data():
    for index,dic in enumerate(data,1):
        print(f"{index}. {dic["category"]}")

while True:
    print("\n--- Expense Tracker APP ---")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Update Expenses")
    print("4. Calculate Total Expenses")
    print("5. Delete Expenses")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        show_data()

        id=int(input("Enter ID of the category to Add Expenses: "))
        amount=int(input("Enter Amount to Add: "))

        found = False
    
        for item in data:
            if item["id"] == id:
                item["amount"] += amount
                save_data()
                print(f"Amount Added Successfully to {item['category']}!")
                found = True
                break

        if not found:
            print("Error: Please enter a valid ID.")
    
    elif choice=="2":
        print("Your Expenses for each Category are:- ")

        for index,dic in enumerate(data,1):
            print(f"{index}. {dic["category"]} : {dic["amount"]}")
    
    elif choice=="3":
        show_data()
        id=int(input("Enter ID of the category to Update Expenses: "))

        found= False

        for item in data:
            if item["id"]==id:
                amount=int(input("Enter Exact Amount to Update: "))
                item["amount"]=amount
                save_data()
                print("Amount Updated Successfully!")
                found=True
                break

        if not found:
            print("Error: Please enter a valid ID.")

    elif choice=="4":
        total_expense=0
        for items in data:
            total_expense+=items["amount"]
        print(f"Your Total Expenses are: {total_expense}")

    elif choice=="5":
        show_data()

        id=int(input("Enter ID of the category to Delete Expenses: "))

        found=False

        for item in data:
            if item["id"]==id:
                item["amount"]=0
                print(f"Expenses for {item["category"]} is deleted.")
                save_data()
                found=True
                break

        if not found:
            print("Error: Please enter a valid ID.")

    elif choice=="6":
        print("Thanks for Using Expenses Tracker!")
        break

    else:
        print("Please Enter a Valid Choice!")