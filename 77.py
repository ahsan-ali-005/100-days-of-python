# Create Library Management System

from datetime import datetime

class LibraryManagementSystem:

    def __init__(self):

        self.admins={
            "ahsan": "ahsan123",
            "admin2": "admin222"
        }

        self.books={
            "Atomic Habits": {"Available": True},
            "Think & Grow Rich": {"Available": True},
            "Python for learners": {"Available": True},
            "Power of Now": {"Available": True},
            "C++ learning": {"Available": True},
            "Sapiens": {"Available": True}
        }

        self.issued_books={}

    def admin_login(self):

        username=input("Enter your username: ")
        password=input("Enter your password: ")

        if username in self.admins and self.admins[username]==password:
            print("Login Successfull!")
            return True
        else:
            print("Invalid Credentials!")
            return False
    
    def add_book(self):
        title=input("Enter Title of Book: ")
        
        self.books[title]= {"Available": True}
        print("Book Added Successfully.")
        return
    
    def del_book(self):
        title=input("Enter Title of book to delete: ")

        if title not in self.books:
            print("No Book Availabe to Delete!")
            return
        
        else:
            del self.books[title]
            print("Book Deleted Successfull.")
            return
    
    def issue_book(self):
        title=input("Enter Book Name: ")

        if title not in self.books:
            print("Book not Available")
            return
        elif title in self.books and self.books[title]["Available"]==False:
            print("Book not Available Right Now! Already Issued.")
            return
        else:
            lender=input("Enter Lender Name: ")
            cnic=input("Enter Lender CNIC: ")
            date_of_issue = datetime.now()
            admin=input("Enter your username(admin): ")

            self.issued_books[title]={
                "lender": lender,
                "lender_cnic": cnic,
                "date": date_of_issue,
                "admin": admin
            }

            self.books[title]["Available"]=False

            print("Book Issued Successfull.")
            return
        
    def view_books(self):

        for i, book in enumerate(self.books,1):
            status= "Available" if self.books[book]["Available"]==True else "Unavailable"
            print(f"{i}. {book}-{status}")
        
    def search_book(self):
        title=input("Enter title of the book: ")

        if title in self.books and self.books[title]["Available"]==True:
            print("Yes Book is Available Right Now!")
            return
        elif title in self.books and self.books[title]["Available"]==False:
            print("Library Has this book but issued Right Now!")
            return
        else:
            print("Book not Present!")
            return
        
    def return_book(self):
        title=input("Enter Book title: ")
        cnic=input("Enter your cnic: ")

        if title not in self.issued_books:
            print("This book was not issued!")
            return
        if self.issued_books[title]["lender_cnic"]==cnic:

            del self.issued_books[title]
            self.books[title]["Available"]=True
            print("Book Returned Successful.")
        else:
            print("Please Enter a Valid cnic.")



lms=LibraryManagementSystem()

while True:
    print(f"{"*" * 10} Welcome to Library System! {"*" * 10}")
    print("1==> Admin Login")
    print("2==> View All Books")
    print("3==> Search for a Specific Book")
    print("4==> Return Book")
    print("5==> Exit")


    choice=input("Enter Choice: ")


    if choice=="1":

        if lms.admin_login():

            while True:
                print(f"{"*" * 10} Welcome to Admin Dashboard! {"*" * 10}")
                print("1==> Add a Book")
                print("2==> Delete a Book")
                print("3==> Issue Book")
                print("4==> Logout!")

                op=input("Enter Choice: ")

                if op=="1":
                    lms.add_book()
                
                elif op=="2":
                    lms.del_book()
                
                elif op=="3":
                    lms.issue_book()
                elif op=="4":
                    print("Logging Out...")
                    print("Goood By!")
                    break
                else:
                    print("Please Enter a Valid Choice!")

    elif choice=="2":
        lms.view_books()
        
    elif choice=="3":
        lms.search_book()
    elif choice=="4":
        lms.return_book()
    elif choice=="5":
        print("Shutting Down!")
        print("By!")
        break
    else:
        print("Enter Valid Choice!")
