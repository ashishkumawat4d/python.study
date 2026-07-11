contacts = {}

while True:
    print("press 1 to Create Contact")
    print("press 2 to View All Contacts")
    print("press 3 to Search Contact")
    print("press 4 to Update Contact")
    print("press 5 to Delete Contact")
    print("press 6 to Count Contacts")
    print("press 7 to Exit")

    choice = input("Enter your choice: ")

   
    if choice == "1":
        name = input("Enter Name: ")
        if name in contacts:
            print("Contact already exists!")
        else:
            age = int(input("Enter Age: "))
            email = input("Enter Email: ")
            mobile = input("Enter Mobile Number: ")
            contacts[name] = {
                "age": age,
                "email": email,
                "mobile": mobile
            }
            print("Contact added successfully!")


    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts available.")
        else:
            for name, info in contacts.items():
                print(f"Name   : {name}")
                print(f"Age    : {info['age']}")
                print(f"Email  : {info['email']}")
                print(f"Mobile : {info['mobile']}")
    

    elif choice == "3":
        name = input("Enter contact name: ")
        if name in contacts:
            info = contacts[name]
            
            print(f"Name   : {name}")
            print(f"Age    : {info['age']}")
            print(f"Email  : {info['email']}")
            print(f"Mobile : {info['mobile']}")
        else:
            print("Contact not found!")





    elif choice == "4":
        name = input("Enter contact name to update: ")
        if name in contacts:
            age = int(input("Enter new Age: "))
            email = input("Enter new Email: ")
            mobile = input("Enter new Mobile Number: ")
            contacts[name] = {
                "age": age,
                "email": email,
                "mobile": mobile
            }
            print("Contact updated successfully!")
        else:
            print("Contact not found!")



    elif choice == "5":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")





    elif choice == "6":
        print(f"Total Contacts: {len(contacts)}")



    elif choice == "7":
        print("Thank you for using Contact Book!")
        break
    
    else:
        print("Invalid Choice! Please try again.")
            
    
