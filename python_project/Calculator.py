
def addition(a,b):
    print(f"your total is {a+b}")
    

def substraction(a,b):
    print(f"your answer is {a-b}")
    



def multiplection(a,b):
    print(f"your answer is {a*b}")
    

def division(a,b):
    try:
        print(f"your answer is {a/b}")
    
    except Exception as err:
        print(f"there is a error as {err}")



print("note: ")
print("press 1 for addition")
print("press 2 for Substraction")
print("press 3 for multiplication")
print("press 4 for dividion")

check = int(input(" please tell your responce :"))


if check == 1:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    
    addition(num1,num2)


if check == 2:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))

    substraction(num1,num2)



if check == 3:
     num1 = int(input("enter first number"))
     num2 = int(input("enter second number"))

     multiplection(num1,num2)


if check == 4:
     num1 = int(input("enter first number"))
     num2 = int(input("enter second number"))

     division(num1,num2)



