habits = {}

while True:
    print("1. Add Habit")
    print("2. Mark Habit Complete")
    print("3. View Habits")
    print("4. Search Habit")
    print("5. Delete Habit")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        habit = input("Enter habit name: ")

        if habit in habits:
            print("Habit already exists.")
        else:
            habits[habit] = "Not completed"
            print("Habit added successfully.")

    elif choice == 2:
        habit = input("Enter habit name: ")

        if habit in habits:
            habits[habit] = "habit completed"
            print("Habit marked as completed.")
        else:
            print("Habit not found.")

    elif choice == 3:
        if habits:
            print("Your Habits ")

            for habit, count in habits.items():
                print(f"{habit} : {count} ")
        else:
            print("No habits available.")

    elif choice == 4:
        habit = input("Enter habit name to search: ")

        if habit in habits:
            print(f"{habit} has been completed {habits[habit]} .")
        else:
            print("Habit not found.")

    elif choice == 5:
        habit = input("Enter habit name to delete: ")

        if habit in habits:
            del habits[habit]
            print("Habit deleted successfully.")
        else:
            print("Habit not found.")

    elif choice == 6:
        print("Thank you for using Habit Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")