    
D = {}





while True:


     print("press 1 to Add Item ")
     print("press 2 to Delete Item")
     print("press 3 to Search Item")
     print("press 4 to View Shopping List")
     print("press 5 to Update Item")
     print("press 6 to Calculate Total Cost")
     print("press 7 to  Exit")


     choice = int(input("enter your choice : "))

     if choice == 1:
          
          item = input("enter Item : ")
          ammount = int(input("enter ammount : "))
          if item in D:
               print("item alredy added")
          D[item] = ammount
          print(D)
          print(f"{item} added successfully ")
          

     if choice == 2:
          item = input("enter the name of the item :  ")
          if item in D:
               del D[item]
          else:
               print("no such item foung ")

     if choice == 3:
          item = input("enter the name of item to search  : ")
          if item in D:
            print(D[item])
          else:
               print("no such item foung ")

     if choice == 4:
          print(D) 
          

     
     if choice == 5:
          item = input("enter the item that you want to update  ")
          if item in D:
               ammount = input("enter the new ammount ")
          D[item] = ammount
          print("updated successfully ")

     if choice == 6:
          if choice == 6:
              total = sum(D.values())
              print(f"Total Cost:, {total}")

     if choice == 7:
          print("thanks for using shopping cart ")
          break



     else:
          print("invalid choice !")



          


        


