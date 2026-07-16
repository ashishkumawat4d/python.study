import json

vault = {}

try:
    with open("vault.json","r") as file:
        vault = json.load(file)

except FileNotFoundError:
    vault = {}



def save():
    with open("vault.json","w") as file:
        json.dump(vault,file,indent=3)
        

def add_password():
    web = input("Enter website name : ")
    if web in vault:
        print(f"password of this website: '{web}' alredy saved ")
    else:
        user = input("Enter user name : ")
        password = input("Enter password : ")
    
        vault[web] = {
            "username": user,
            "password": password
        }
        save()

        print("password saved successfully ")



def view_password():
    web = input("enter website name : ")
    if web in vault:
        print(vault[web])
    else:
        print("no password found! ")
        

def update_password():
    web = input("Enter website : ")

    if web in vault:
        print(vault)
        print(vault[web])
        print(f"Old password : {vault[web]['password']}")
        new_pass = input("Enter new password : ")

        vault[web]['password'] = new_pass



def delete_password():
    web = input("Enter website : ")
    print(vault)
    print(vault[web])
    print(f"password : {vault[web]['password']}")


    if web in vault:
        
        del vault[web]
        print("password deleted successfully ")



    else:
        print("no password found !")



while True:
    print("\n-------PASSWORD VAULT-------")
    print("press 1 Add Password")
    print("press 2 View Passwords")
    print("press 3 Update Password")
    print("press 4 Delete Password")
    print("press 5 Exit")
    
    
    check = int(input("Enter your choice : "))
    
    if check == 1:
        add_password()
    
    
    if check == 2:
        view_password()



    if check == 3:
        update_password()

    
    if check == 4:
        delete_password()

    if check == 5:
        print("thanks for using Password Vault")

        
    
        