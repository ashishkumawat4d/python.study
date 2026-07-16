import json

try:
    with open("students.json","r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = {}


def save():
    with open("students.json","w") as file:
        json.dump(students,file,indent=3)





def add_student():
    name = input("Enter the name of student :")
    if name in students:
        print("Name alredy exist")
    else:
        clas = input("enter class :")
        age = int(input("Enter age :"))
        parent = input("Enter the name of parents :")
        email = input("enter email")
        contact = int(input("Enter contact number of parents"))

        students[name] = {
            'class' : clas,
            'age': age,
            'parent':parent,
            'email':email,
            'contact':contact

        }
        save()
        print("student added successfully")



def view_all_students():

     if len(students) == 0:
        print("No students found.")
        return
 
     else:
        for name, details in students.items():
            print("-" * 35)
            print(f"Name    : {name}")
            print(f"Class   : {details['class']}")
            print(f"Age     : {details['age']}")
            print(f"Parent  : {details['parent']}")
            print(f"Email   : {details['email']}")
            print(f"Contact : {details['contact']}")
        print("-" * 35)
    

def search_student():
    name = input("Enter the name of student : ")
    if name in students:
        print(students[name])
    else:
        print("No students found!")



def update_student():
    name = input("Enter the name of student :")
    if name in students:
        print("previous data", students[name])
        clas = input("Update class :")
        age = int(input("Update age :"))
        parent = input("Enter the name of parents :")
        email = input("Update email")
        contact = int(input("Update contact number of parents"))

        students[name] = {
            'class' : clas,
            'age': age,
            'parent':parent,
            'email':email,
            'contact':contact
        }
        save()
        print("Data saved successfully")
       

def Delete_Student():
    name = input("Enter the name of the student : ")
    if name in students:
        del students[name]
        print("deleted successfully")
    else:
        print("No student found!")


def count():
    num = len(students)
    print(f"total students : {num}")


while True:

    print("------ STUDENT MANAGER ------ ")
    
    print("press 1 to Add Student")
    print("press 2 to View All Students")
    print("press 3 to Search Student")
    print("press 4 to Update Student")
    print("press 5 to Delete Student")
    print("press 6 to Count Total Students")
    print("press 7 to Exit")
    
    print("---------------------------")
    
    check = int(input("enter your choice :"))
    
    
    if check == 1:
        add_student()
    
    if check == 2:
        view_all_students()
    
    if check == 3:
        search_student()
    
    if check == 4:
        update_student()
    
    if check == 5:
        Delete_Student()

    if check == 6:
        count()

    if check == 7:
        print("Thanks for using Student Manager ")


