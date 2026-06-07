# Create Inventory management system


class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Inventory:

    def __init__(self):
        self.products = {}  

    def add_product(self):
        name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))

        if name in self.products:
            self.products[name].quantity += quantity
            print("Product exists, quantity updated.")
        else:
            self.products[name] = Product(name, quantity)
            print("Product added.")

    def remove_product(self):
        name = input("Enter Product Name to remove: ")

        if name in self.products:
            del self.products[name]
            print("Product removed.")
        else:
            print("Product not found!")

    def update_quantity(self):
        name = input("Enter Product Name: ")

        if name in self.products:
            new_quantity = int(input("Enter new quantity: "))
            self.products[name].quantity = new_quantity
            print("Quantity updated.")
        else:
            print("Product not found!")

    def view_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("\nInventory List:")
            for product in self.products.values():
                print(f"{product.name} : {product.quantity}")


inventory = Inventory()

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Update Quantity")
    print("4. View Inventory")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        inventory.add_product()
    elif choice == "2":
        inventory.remove_product()
    elif choice == "3":
        inventory.update_quantity()
    elif choice == "4":
        inventory.view_inventory()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")