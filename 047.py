# Create ShoppingCart class

class Product:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity

class Shopping_Cart:

    def __init__(self):
        self.items={}

    def add_to_cart(self):
        name=input("Enter Name of Product: ")
        quantity=int(input("Enter Quantity of Product: "))

        if name in self.items:
            self.items[name].quantity += quantity
            print("Product exists, quantity updated.")
        else:
            self.items[name]=Product(name,quantity)
            print("Product added to Cart.")

    def update_quantity(self):
        name=input("Enter the Name of the Product to update quantity: ")
        new_quantity=int(input("Enter Quantity to update: "))

        if name not in self.items:
            self.items[name]=Product(name,new_quantity)
            print("Product Added to cart with your quantity.")
        else:
            self.items[name].quantity = new_quantity
            print("New Quantity Updated.")

    def remove_product(self):
        name=input("Enter the Name of the Product to remove: ")

        if name not in self.items:
            print("Product Doesn't Exist in Cart.")
        else:
            del self.items[name]
            print("Product Removed.")
        

    def view_cart(self):
        if not self.items:
            print("Cart is Empty!")
        else:
            for product in self.items.values():
                print(f"{product.name} : {product.quantity}")


cart = Shopping_Cart()

while True:

    print("1. Add Products to Cart")
    print("2. Increase/Decrease Quantity")
    print("3. Remove Product")
    print("4. View Cart")
    print("5. Exit")

    choice=input("Enter your Choice: ")

    if choice=="1":
        cart.add_to_cart()
    elif choice=="2":
        cart.update_quantity()
    elif choice=="3":
        cart.remove_product()
    elif choice=="4":
        cart.view_cart()
    elif choice=="5":
        break
    else:
        print("Invalid Input Choice!")
