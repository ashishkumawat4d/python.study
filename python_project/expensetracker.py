expenses = {}


def addexpense():
    category = input("Enter category: ")
    amount = int(input("Enter amount: "))

    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

    print("Expense added successfully ")


def viewexpenses():
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("Expenses :")
        for category, amount in expenses.items():
            print(category, ":", amount)


def searchexpense():
    category = input("Enter category to search: ")

    if category in expenses:
        print(category, ":", expenses[category])
    else:
        print("Category not found.")


def deleteexpense():
    category = input("Enter category to delete: ")

    if category in expenses:
        del expenses[category]
        print("Expense deleted successfully!")
    else:
        print("Category not found.")


def totalexpense():
    total = sum(expenses.values())
    print("Total Expense:", total)


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Expense")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addexpense()

    elif choice == 2:
        viewexpenses()

    elif choice == 3:
        searchexpense()

    elif choice == 4:
        deleteexpense()

    elif choice == 5:
        totalexpense()

    elif choice == 6:
        
        break

    else:
        print("Invalid choice.")

