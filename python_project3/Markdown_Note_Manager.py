import json


try:
    with open("notes.json", "r") as file:
        notes = json.load(file)
except FileNotFoundError:
    notes = {}


def save():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def create_note():
    title = input("Enter note title: ")
    print("Write your note (Type END to finish):")

    content = ""

    while True:
        line = input()

        if line == "END":
            break

        content += line + "\n"

    notes[title] = content
    save()
    print("Note saved.")


def view_note():
    title = input("Enter note title: ")

    if title in notes:
        print("----- Note -----")
        print(notes[title])
    else:
        print("Note not found.")


def view_all_notes():
    if len(notes) == 0:
        print("No notes found.")
    else:
        print("\nNotes:")
        for title in notes:
            print(title)


def delete_note():
    title = input("Enter note title: ")

    if title in notes:
        del notes[title]
        save()
        print("Note deleted.")
    else:
        print("Note not found.")


while True:
    print("-----Markdown Note Manager-----")
    print("press 1 to Create Note")
    print("press 2 to View Note")
    print("press 3 to View All Notes")
    print("press 4 to Delete Note")
    print("press 5 to Exit")

    check = int(input("Enter choice: "))

    if check == 1:
        create_note()

    elif check == 2:
        view_note()

    elif check == 3:
        view_all_notes()

    elif check == 4:
        delete_note()

    elif check == 5:
        break

    else:
        print("Invalid choice!")