import json

FILE_NAME = "notes.json"

try:
    with open(FILE_NAME, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"notes": []}

def save():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def display_notes():
    if len(data["notes"]) == 0:
        print("No notes found.")
        return

    print("\n----- NOTES -----")
    for note in data["notes"]:
        print(note)


def search_word():
    word = input("Enter word to search: ").lower()

    found = False

    for line_number, note in enumerate(data["notes"], start=1):
        if word in note.lower():
            print(f"Line {line_number}: {note}")
            found = True

    if not found:
        print("Word not found.")


def count_occurrences():
    word = input("Enter word: ").lower()

    count = 0

    for note in data["notes"]:
        count += note.lower().count(word)

    print(f'"{word}" appears {count} time(s).')


def show_line_numbers():
    word = input("Enter word: ").lower()

    found = False

    for line_number, note in enumerate(data["notes"], start=1):
        if word in note.lower():
            print(f"Found on Line {line_number}")
            found = True

    if not found:
        print("Word not found.")


def replace_word():
    old = input("Enter word to replace: ")
    new = input("Enter new word: ")

    found = False

    for i in range(len(data["notes"])):
        if old in data["notes"][i]:
            data["notes"][i] = data["notes"][i].replace(old, new)
            found = True

    if found:
        save()
        print("Word replaced successfully!")
    else:
        print("Word not found.")


while True:

    print("------TEXT FILE SEARCH TOOL-------")
    print("press 1 to Display Notes")
    print("press 2 to Search Word")
    print("press 3 to Count Occurrences")
    print("press 4 to Show Line Numbers")
    print("press 5 to Replace Word")
    print("press 6 to Exit")


    choice = input("Enter your choice : ")

    if choice == "1":
        display_notes()

    elif choice == "2":
        search_word()

    elif choice == "3":
        count_occurrences()

    elif choice == "4":
        show_line_numbers()

    elif choice == "5":
        replace_word()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")