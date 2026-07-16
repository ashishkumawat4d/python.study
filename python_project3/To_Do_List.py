import json


try:
    with open("todolist.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


def save():
    with open("todolist.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    task = input("Enter task: ")

    if task in tasks:
        print("Task already exists.")
    else:
        tasks.append(task)
        save()
        print("Task added successfully.")


def view_tasks():

    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\n------ TO DO LIST ------")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")



def delete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number: "))

        if 1 <= number <= len(tasks):

            removed = tasks.pop(number - 1)

            save()

            print(f"{removed} deleted successfully.")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")






def search_task():

    keyword = input("Enter task to search: ").lower()

    found = False

    for task in tasks:

        if keyword in task.lower():

            print(task)

            found = True

    if not found:
        print("Task not found.")



while True:



    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Search Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        search_task()

    elif choice == "5":
        save()
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")