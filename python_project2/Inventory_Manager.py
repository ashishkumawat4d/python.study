inventory = {}

while True:
    print("press 1 to Add Product")
    print("press 2 to View Products")
    print("press 3 to Search Product")
    print("press 4 to Update Quantity")
    print("press 5 to Delete Product")
    print("press 6 to Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        inventory[product] = quantity
        print("Product added successfully")

    if choice == 2:
        if inventory:
            for product, quantity in inventory.items():
                print(product, ":", quantity)
        else:
            print("Inventory is empty.")

    if choice == 3:
        product = input("Enter product name: ")
        if product in inventory:
            print("Quantity =", inventory[product])
        else:
            print("Product not found.")

    elif choice == 4:
        product = input("Enter product name: ")
        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Quantity updated!")
        else:
            print("Product not found.")

    elif choice == 5:
        product = input("Enter product name: ")
        if product in inventory:
            del inventory[product]
            print("Product deleted!")
        else:
            print("Product not found.")

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")