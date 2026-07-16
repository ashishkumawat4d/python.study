# D = {}



# def addnotes():
#     Title = input("Enter the title : ")
#     content = input("enter content : ")
#     if Title in D:
#         print("Title alredy exist ")
#     else:
#         D[Title] = content
#         print("note saved successfully ")
# def View_All_Notes():
#     print("-" * 30)
#     for title, content in D.items():
#       print("Title:", title)
#       print("Content:", content)
#       print("-" * 30)
          
    
# def Search_Note():
#     title = input("Enter the title to search note;"    )
#     if title in D:
#       print("Title: ", title)
#       print("Content:" ,D[title])
#     else:
#         print(f"no title exist as {title} ")

    
# def Edit_Note():
#     title = input("enter the title of the note :  ")
#     if title in D:
#         print("current content :", D[title])
#         newcontent = input("enter new content :  ")
#         D[title] = newcontent
#     else:
#         print(f"title {title} not exist ")    


# def delnote():
#     title = input("enter the title of the note :  ")
#     if title in D:
#         del D[title]
#         print("note deleted successfully")
#     else:
#         print("no note exist ")

# def count():
#     print("total notes: " ,len(D))





# while True:


    
    
    
    
#     print("press '1' to Add Notes")
#     print("press '2' to View All Notes")
#     print("press '3' to Search Note")
#     print("press '4' to Edit Note")
#     print("press '5' to Delete Note")
#     print("press '6' to Count Notes")
#     print("press '7' to Exit ")
    
    

    
#     check = int(input("enter your choice :  "))
    
#     if check == 1:
#         addnotes()

#     elif check == 2:
#         View_All_Notes()

#     elif check == 3:
#         Search_Note()

#     elif check == 4:
#         Edit_Note()

#     elif check == 5:
#         delnote()


    # elif check == 6:
    #     count()
    

    # elif check == 7:
    #     print("thanks for using Notes App")
    #     break


    # else:
    #     print("invalid choice !")



# ------------------------- USING JSON ----------------------------



import json
try:
    with open("notes.json","r") as file:
        D = json.load(file)
    
except Exception as err:
    print(f"an error occurred as {err}")


def save_notes():
    with open("notes.json","w") as file:
        json.dump(D,file)




def add_note():
    title = input("Enter title: ")
    content = input("Enter content: ")

    if title in D:
        print("Title already exists!")
    else:
        D[title] = content
        save_notes()          
        print("Note saved!")



def view_notes():
    if not D:
        print("No notes available.")
        return

    for title, content in D.items():
        print("-" * 30)
        print("Title :", title)
        print("Content :", content)
        print("-" * 30)



while True:
    print("\npress 1 to Add Note")
    print("press 2 to View Notes")
    print("press 3 to Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()


    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


