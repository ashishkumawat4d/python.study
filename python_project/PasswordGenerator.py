import random
import string

def generatepass(length):
    char = (
       string.ascii_letters +     
        string.digits +             
        string.punctuation  


    )

    


    password = ""
    for i in range(length):
        password += random.choice(char)
    
    return password


try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")

    else:
        password = generatepass(length)
        print("your Generated Password:")
        print(password)

except Exception as err:
    print(f"there is a error as {err}")