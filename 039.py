# Bank System with Transfer System

class Bank:
    
    bank_name="Alfalah Bank"
    branch_code="0265"


    def __init__(self,acc_no,title,balance):
        self.acc_no=acc_no
        self.title=title
        self.balance=balance
        self.history=[]


    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} Deposited Successfully.")
        self.history.append(f"{amount} Deposited to {self.acc_no}.")


    def withdraw(self,amount):
        self.balance-=amount
        print(f"{amount} Withdrawn Successfully.")
        self.history.append(f"{amount} Withdrawn from {self.acc_no}.")


    def current_balance(self):
        print(f"Your Balance is {self.balance}")
    

    def show_history(self):
        if not self.history:
            print("No Transactions Yet.")
        else:
            for i,t in enumerate(self.history,1):
                print(f"{i}. {t}")

    def transfer(self,amount,receiver):
        if amount<=0:
            print("Invalid Amount!")
            return

        if amount>self.balance:
            print("You have Insufficient Balance...")
            return

        self.balance-=amount
        receiver.balance+=amount
        print(f"{amount} Transferred Successfully.")

        self.history.append(f"Transferred {amount} to {receiver.acc_no}")
        receiver.history.append(f"Received {amount} from {self.acc_no}")
        


    

accounts={}

while True:
    print(f"======== Welcome to {Bank.bank_name}. Branch code: {Bank.branch_code} ========")
    print("1. Create Account")
    print("2. Access My Account")
    print("3. Exit")

    choice=input("Enter Your Option: ")

    if choice=="1":
        acc_no=input("Enter Account Number: ")
        if acc_no in accounts:
            print("Account Already Exists...")
            continue

        title=input("Enter Account Title: ")

        try:
            balance=int(input("Enter Starting Balance: "))
        except:
            print("Invalid Amount!")
            continue

        accounts[acc_no]=Bank(acc_no,title,balance)
        print("Account Created Successfully!")

    elif choice=="2":
        acc_no=input("Enter Account Number: ")
        if acc_no not in accounts:
            print("Account Doesn't Exist...")
            continue

        while True:

            print("1. Deposit to Account")
            print("2. Withdraw from Account")
            print("3. Transfer Funds")
            print("4. Check Account Balance")
            print("5. Check Account History")
            print("6. Back to Main Menu")

            op=input("Enter Operation: ")

            if op=="1":
                
                amount=int(input("Enter Amount: "))
                if amount<=0:
                    print("Invalid Amount!")
                    continue

                accounts[acc_no].deposit(amount)

            elif op=="2":
                amount=int(input("Enter Amount: "))

                if amount<=0 or amount> accounts[acc_no].balance:
                    print("Please Enter Valid Amount...") 
                    continue

                accounts[acc_no].withdraw(amount)

            elif op=="3":

                receiver=input("Enter Receiver Account Number: ")
                if receiver not in accounts:
                    print("Account Doesn't Exists...")
                    continue

                if receiver == acc_no:
                    print("Can't Transfer to Same Account...")
                    continue

                amount=int(input("Enter Amount: "))

                accounts[acc_no].transfer(amount, accounts[receiver])
                

            elif op=="4":
                 accounts[acc_no].current_balance()
            
            elif op=="5":
                 accounts[acc_no].show_history()

            elif op=="6":
                break

            else:
                print("Invalid Operation!")

    elif choice=="3":
        print("Thanks For Using Bank System.")
        break

    else:
        print("Invalid Choice!")



                
