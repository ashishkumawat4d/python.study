import os

folder = input("Enter folder path: ")

while True:
    print("--- File Statistics Analyzer ---")
    print("press 1 to Count Files")
    print("press 2 to Count Folders")
    print("press 3 to Total File Size")
    print("press 4 to Exit")

    check = nt(input("Enter your choice: "))

    if check == 1:
        count = 0
        for item in os.listdir(folder):
            path = os.path.join(folder, item)
            if os.path.isfile(path):
                count += 1
        print("Total Files:", count)

    elif check == 2:
        count = 0
        for item in os.listdir(folder):
            path = os.path.join(folder, item)
            if os.path.isdir(path):
                count += 1
        print("Total Folders:", count)

    elif check == 3:
        size = 0
        for item in os.listdir(folder):
            path = os.path.join(folder, item)
            if os.path.isfile(path):
                size += os.path.getsize(path)
        print("Total Size:", round(size / 1024, 2), "KB")

    elif check == 4:
        print("Thanks for using File statistics analyzer!")
        break

    else:
        print("Invalid choice!")