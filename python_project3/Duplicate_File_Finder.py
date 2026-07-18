import os
import json
import hashlib


try:
    with open("files.json", "r") as file:
        files = json.load(file)
except FileNotFoundError:
    files = {}

folder = input("Enter folder path: ")


for filename in os.listdir(folder):

    path = os.path.join(folder, filename)

    if os.path.isfile(path):

        with open(path, "rb") as file:
            data = file.read()

        file_hash = hashlib.md5(data).hexdigest()

        if file_hash in files:
            print("\nDuplicate Found!")
            print("Original :", files[file_hash])
            print("Duplicate:", path)

        else:
            files[file_hash] = path

# Save data to JSON
with open("files.json", "w") as file:
    json.dump(files, file, indent=4)

print("\nScan completed!")