import json

try:
    with open("income.json","r") as file:
        income = json.load(file)
except FileNotFoundError:
    income = {}



def save1():
    with open("income.json","w") as file:
        json.dump(income,file,indent=3)
        

    

try:
    with open("expense.json","r") as file:
        expense = json.load(file)
except FileNotFoundError:
    expense = {}



def save2():
    with open("expense.json","w") as file:
        json.dump(expense,file,indent=3)
        




def add_income():
    source = input("Enter source of income : ")
    if source in income:
        print("source alredy exist, you can update incom ")
    else:
         inc =   float(input("Enter income : "))
         income[source] = inc
         save1()
         print("income added successfully ")





def add_expense():
    category = input("\nEnter category where you have spent the money : ")
    
    if category in expense:
        print("category alredy exist, you can update expense ")
    else:
         amount =   float(input("Enter amount : "))
         expense[category] = amount
         save2()
         print("Expense added successfully ")





def view_income():
    print("press 1 to view all incom and sources")
    print("press 2 to search source and income")
    
    choice = int(input("Enter your choice : "))

    if choice == 1:
        print("--- income details ---")
        for index ,task in enumerate(income,start=1):
            print(f"{index}. {income}")
    elif choice == 2:
        source = input("Enter the source of income : ")
        if source in income:
            print(income[source])
        else:
            print("no source found !")
    else:
        print("invalid choice!")





def view_expense():
    print("\npress 1 to view all Expenses")
    print("press 2 to search Expenses")
    
    choice = int(input("Enter your choice : "))

    if choice == 1:
        print("--- expenses details ---")
        for index ,task in enumerate(income,start=1):
            print(f"{index}. {expense}")
    elif choice == 2:
        category = input("Enter the category where you have spent the money : ")
        if category in expense:
            print(expense[category])
        else:
            print("no expense found ")
    else:
        print("invalid choice!")
    




def Update_Expense():
    category = input("Enter the category of expense : ")
    if category in expense:
        print("old expense:", expense[category])
        amount = float(input("Enter ne amount : "))
        expense[category] = amount
        save2()
        print("Expense updated successfully ")
    else:
        print("No expense found !")
    




def Delete_Expense():
    category = input("Enter the category of expense : ")
    if category in expense:
        del expense[category]
        print("Expense deleted successfully ")
    else:
        print("No expense found !")





def View_Balance():
    total_income = sum(income.values())
    total_expenses = sum(expense.values())

    balance =  total_income - total_expenses

    print(f"your total balance {balance}")




    
def delete_income():
    source = input("Enter the source of income : ")
    if source in income:
        del income[source]
        print("income deleted successfully ")
    else:
        print("No income found !")

    




while True:          
   print("-------- BUDGET TRACKER --------")
   print("press 1 to Add Income")
   print("press 2 to Add Expense")
   print("press 3 to View Income")
   print("press 4 to View Expenses")
   print("press 5 to Update Expense")
   print("press 6 to Delete Expense")
   print("press 7 to View Balance")
   print("press 8 to delete income")
   print("press 9 to Exit")
   
   check = int(input("Enter your choice"))
   
   if check == 1:
       add_income()
   
   elif check == 2:
       add_expense()
   
   elif check == 3:
       view_income()

   elif check == 4:
       view_expense()

   elif check == 5:
       Update_Expense()
    
   elif check == 6:
        Delete_Expense()

   elif check == 7:
       View_Balance()
       
   elif check == 8:
       delete_income()

   elif check == 9:
       print("Thanks for using Budget Tracker")
       break
   
   else:
       print("Invalid Choice !")

       

