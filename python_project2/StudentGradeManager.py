D = {}

while True:
    print("press 1 to add student")
    print("press 2 to view all students")
    print("press 3 to update student marks")
    print("press 4 to delete a student's record.")
    print("press 5 to Search Students")
    print("press 6 to count student")
    #  print("press 7 to find highest and lowest scorer ")
    
    
    
    
    check = int(input("enter your choice  :  "))
    
    
    if check == 1:
        name = input("enter the name of the student : ")
        if name in D:
            print("alredy saved")
        else:
            maths = int(input("Enter mathematics marks out of 100 : "))
            science = int(input("Enter Science marks  out of 100 : "))
            english = int(input("Enter English marks  out of 100 : "))
            
           
            D[name] = {
                'maths':maths ,
                'science':science,
                'english':english
            }
    
            print("Marks added successfully!")
    
            print(D)


    if check == 2:
        print(D)
    

    if check == 3:
        name = input("Enter the name of the student : ")
        if name in D:
             maths = int(input("new maths marks "))
             science  = int(input("new science marks "))
             english = int(input("new english marks "))
             print("saved successfully")
        else:
            print("student dose not exist")
    

    if check == 4:
        name = input("Enter the name of the student : ")
        if name in D:
           del D[name]
           print("record deleted successfully : ")
        else:
            print("student dose not exist")

    
    if check == 5:
        name = input("enter the name of the student : ")
        if name in D:
            print(D[name])

        else:
            print("student dose not exist")

    
    if check == 6:
        print(len(D))


    # if check == 7:
        



    

        

        




             
