# Bank System

class Bank:

    bank_name = "Alfalah Bank"
    bank_branch = "0265"

    def __init__(self, account_no, title, balance):
        self.account_no = account_no
        self.title = title
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")

    def current_balance(self):
        print(f"Current Balance: {self.balance}")


# Store all users
accounts = {}

while True:

    print(f"\n------ Welcome to {Bank.bank_name}. Branch Code: {Bank.bank_branch}------")
    print("\n------ BANK MENU ------")
    print("1 Create New Account")
    print("2 Select Existing Account")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        acc_no = input("Enter Account Number: ")
        title = input("Enter Account Title: ")
        balance = int(input("Enter Starting Balance: "))

        accounts[acc_no] = Bank(acc_no, title, balance)


        print("Account created successfully.")

    elif choice == "2":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            user = accounts[acc_no]

            while True:

                print("\n--- Account Menu ---")
                print("1 Deposit")
                print("2 Withdraw")
                print("3 Check Balance")
                print("4 Back to Main Menu")

                op = input("Enter operation: ")

                if op == "1":
                    amount = int(input("Enter Amount: "))
                    user.deposit(amount)

                elif op == "2":
                    amount = int(input("Enter Amount: "))
                    user.withdraw(amount)

                elif op == "3":
                    user.current_balance()

                elif op == "4":
                    break

                else:
                    print("Invalid choice.")

        else:
            print("Account not found.")

    elif choice == "3":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice.")