def add_entry():
    entry = input("Write your journal entry: ")

    with open("journal.txt", "a") as file:
        file.write(entry + "\n")

    print("Entry saved successfully!\n")


def view_entries():
    try:
        with open("journal.txt", "r") as file:
            entries = file.readlines()

            if not entries:
                print("No journal entries found.\n")
            else:
                print("\n----- Your Journal -----")
                for i, entry in enumerate(entries, start=1):
                    print(f"{i}. {entry.strip()}")
                print("------------------------\n")

    except FileNotFoundError:
        print("No journal file found.\n")


while True:
    print("=== Journal App ===")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")