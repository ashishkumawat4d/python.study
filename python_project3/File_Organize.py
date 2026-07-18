import json

try:
    with open("files.json", "r") as file:
        folders = json.load(file)
except FileNotFoundError:
    folders = {}

def save():
    with open("files.json", "w") as file:
        json.dump(folders, file, indent=4)


while True:
    print("--- File Organizer ---")
    print("press 1 to Add File")
    print("press 2 to View Files")
    print("press 3 to Search File")
    print("press 4 to Exit")

    check = int(input("Enter your choice: "))

    if check == "1":
        name = input("Enter file name: ")

        if name.endswith(".jpg") or name.endswith(".png"):
            folders[name] = "Images"

        elif name.endswith(".pdf"):
            folders[name] = "PDFs"

        elif name.endswith(".mp3"):
            folders[name] = "Music"

        else:
            folders[name] = "Others"

        save()
        print("File added!")

    elif check == "2":
        if len(folders) == 0:
            print("No files found.")
        else:
            for file, folder in folders.items():
                print(file, "->", folder)

    elif check == "3":
        name = input("Enter file name: ")

        if name in folders:
            print(name, "is in", folders[name])
        else:
            print("File not found.")

    elif check == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")