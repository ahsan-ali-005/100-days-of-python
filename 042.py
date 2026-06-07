# Create Employee salary increment system

class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    
    def increment_salary(self,amount):
        self.salary+=amount
        print(f"The Salary of {self.name} after increment is {self.salary}")


name=input("Enter name of the Employee: ")
salary=int(input("Enter Salary of the Employee: "))
amount=int(input("Enter Amount to Increment: "))

e1=Employee(name,salary)
e1.increment_salary(amount)