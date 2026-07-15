import json
D = {}

while True:

    def addnotes():
        Title = input("Enter the title : ")
        content = input("enter content : ")

        if Title in D:
            print("Title alredy exist ")
        else:
            D[Title] = content
            print("note saved successfully ")

    def View_All_Notes():
        print("-" * 30)
        for title, content in D.items():
          print("Title:", title)
          print("Content:", content)
          print("-" * 30)
              
        

    def Search_Note():
        title = input("Enter the title to search note;"    )
        if title in D:
          print("Title: ", title)
          print("Content:" ,D[title])

        else:
            print(f"no title exist as {title} ")
    

        

    def Edit_Note():
        title = input("enter the title of the note :  ")
        if title in D:
            print("current content :", D[title])
            newcontent = input("enter new content :  ")
            D[title] = newcontent



        else:
            print(f"title {title} not exist ")    

    
    
    def delnote():
        title = input("enter the title of the note :  ")
        if title in D:
            del D[title]
            print("note deleted successfully")
        else:
            print("no note exist ")
    
    def count():
        print("total notes: " ,len(D))

    
    
    
    
    print("press '1' to Add Notes")
    print("press '2' to View All Notes")
    print("press '3' to Search Note")
    print("press '4' to Edit Note")
    print("press '5' to Delete Note")
    print("press '6' to Count Notes")
    print("press '7' to Exit ")
    
    

    
    check = int(input("enter your choice :  "))
    
    if check == 1:
        addnotes()

    if check == 2:
        View_All_Notes()

    if check == 3:
        Search_Note()

    if check == 4:
        Edit_Note()

    if check == 5:
        delnote()


    if check == 6:
        count()
    

    if check == 7:
        print("thanks for using Notes App")
        break


    else:
        print("invalid choice !")
