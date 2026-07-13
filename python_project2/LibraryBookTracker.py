L = []


while True:

   print("press 1 to Add Book ")
   print("press 2 to view all books ")
   print("press 3 to Delete Book ")
   print("press 4 to Count books" )
   print("press 5 to exit ")
   
   
   
   choice = int(input("enter your choice : "))
   
   
   if choice == 1:
       book = input("enter the name of the book : ")
       if book in L:
           print("book alredy exist")
       else:
           L.append(book)
           print("Book saved successfully ")
       
   if choice == 2:
       if len(L) == 0:
           print("no book saved ")

       else:
           print(L)

   if choice == 3:
       book = input("enter the name of the book that you want to delete : ")
       L.remove(book)
       print(f"{book} removed successfully ")

   if choice == 4:
       print(len(L))
    
   if choice == 5:
       print("thanks for using library book tracker ")
       break
    
   else:
       print{"invalid choice "}



