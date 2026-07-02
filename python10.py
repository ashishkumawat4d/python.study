#        Exception Handling
        
#        Errors
        
#        Errors occur due to mistakes in the code that prevent it from
#        running. These can be syntax errors or logical errors.
        
        
#        Indentation Errors
        
#        if you don’t follow indentation ,you will get the error.
        
       
#        These errors cannot be handled. but what can be handled
#        are exceptions.
       
      
      
#        EXCEPTIONS
        
#        Exceptions are unexpected events or errors that occurs
#        during the execution of a program, which disrupts the normal
#        flow of the program.
        
#        example


print("start")
#print(10/0)  # Raises ZeroDivisionError
print("end") #---> this line will never run due to this error

#       Now this is a ZeroDIvisionError and can be counted as
#       Exception and because of this exception the next line cannot
#       be executed.


#       the good part is we can handel them lets see how.



#       So these are the keywords that we use and all these
#       keywords has their separate purpose as mentioned. ̄



#           
#        | **Keyword** | **Purpose**                                                                                                               |
#           
#        | ----------- | ------------------------------------------------------------------------------------------------------------------------  |
#            
#        | `try`        | Contains the code that may raise an exception (risky code).                                                              |
#            
#        | `except`     | Catches and handles the exception if it occurs.                                                                          |
#            
#        | `else`       | Executes only if no exception occurs in the `try` block.                                                                 |
#            
#        | `finally`    | Executes whether an exception occurs or not. Used for cleanup tasks (e.g., closing files or database connections).       |
#            
#        | `raise`      | Manually raises an exception. Used to create custom errors or trigger built-in exceptions.                               |



#     EXAMPLE

# try and except

a = int(input("tell your number"))

try:
    print(10/a)

except ZeroDivisionError:
    print("sorry you nannot divide by zero")


print("next line executed")
 





# OR







a = int(input("tell your number"))

try:
    print(10/a)

except Exception as err:
    print(f"sorry there is a error as {err}")


print("next line executed")
 








 # else

a = int(input("tell your number"))

try:
    print(10/a)

except Exception as err:
    print(f"sorry there is a error as {err}")

else:
    print("good there is no exception")




print("next line executed") 





 # finally





try:
    print(10 / 0)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Program End")




     # raise - (we can raise a error by ourselfs)



age = int(input("tell your age :  "))

if age < 18:
    raise ValueError("your age must be greater then 18 ")
else:
    print("welcome to the club")

print("the club will start soon" )



