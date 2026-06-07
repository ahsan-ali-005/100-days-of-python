# ATM Simulation System

class ATM:

    def __init__(self, user, cards):
        self.user = user
        self.cards = cards

    def withdraw(self):
        amount = int(input("Enter Amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.user["balance"]:
            print("Insufficient Balance!")
        else:
            self.user["balance"] -= amount
            print(f"{amount} Withdrawn Successfully.")

    def deposit(self):
        amount = int(input("Enter Amount to deposit: "))

        if amount <= 0:
            print("Invalid amount!")
        else:
            self.user["balance"] += amount
            print(f"{amount} Deposited Successfully.")

    def transfer(self):
        reciever_no = input("Enter Receiver Card no: ")

        if reciever_no not in self.cards:
            print("Card doesn't exist in our Database.")
            return

        amount = int(input("Enter Amount to transfer: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.user["balance"]:
            print("Insufficient Balance!")
        else:
            reciever = self.cards[reciever_no]
            self.user["balance"] -= amount
            reciever["balance"] += amount
            print(f"{amount} Transferred Successfully to {reciever_no}.")

    def current_balance(self):
        print(f"Your Balance is: {self.user['balance']}")


# Database
cards = {
    "35201": {"pin": "1111", "balance": 5000},
    "35202": {"pin": "2222", "balance": 10000}
}

# Login System
card = input("Enter Card Number: ")

if card not in cards:
    print("Invalid Card Number.")
else:
    user = cards[card]

    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")

        if pin == user["pin"]:
            print("Authentication Completed. You're Welcome...")
            atm = ATM(user, cards)

            # Menu Loop
            while True:
                print("\n1. Withdraw Money")
                print("2. Deposit Money")
                print("3. Transfer Money")
                print("4. Check Balance")
                print("5. Exit")

                choice = input("Enter Your Choice: ")

                if choice == "1":
                    atm.withdraw()
                elif choice == "2":
                    atm.deposit()
                elif choice == "3":
                    atm.transfer()
                elif choice == "4":
                    atm.current_balance()
                elif choice == "5":
                    print("Thank you for using ATM.")
                    break
                else:
                    print("Invalid Input Choice!")

            break
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")

    if attempts == 0:
        print("Card Blocked due to multiple wrong attempts.")