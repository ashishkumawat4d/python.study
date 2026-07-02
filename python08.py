#        Functions




#        What are functions
#        
#        Functions in Python group reusable code into a block that
#        can be executed by calling the function name. This helps
#        avoid repetition and makes programs modular and readable.
#        
#        
#        There are many in-build functions in python like print(), input()
#        len() etc.
#        
#        
#        But you can create your own function and they are called as
#        user defined functions. To make your own function you have
#        to use def keyword and then name the function. After this
#        you have to call the function using name() and paranthesis.


#        EXAMPLE

def hello():
    print("this is hello function")


hello()  # this will call the fuction
    


#        Functions parameters and arguments


#         parameters are
#         variables listed inside the function definition.

#         For making the function we have to accept inside the
#         parenthesis of the function.


#         EXAMPLE

def sum(a,b):
    print(f"the sum of your number is {a + b}")


sum(2,3)


#        Arguments are the Values passed to a function when it is called

#        EXAMPLE

def greet(name):  # name is a parameter
    print(f"hello, {name}")

greet("ashish")   # "ashish" is an argument


#       first parameter, will always capture first
#       argument and so on. These arguments are called positional
#       argument.





#      Types of Arguments



#      Now there are 3 types of argument that we can pass to
#      parameters. positional argument, default argument, keyword argument




def sum(a,b):
    print(f"the sum of your number is {a + b}")

#  positional argument,

sum(2,3) 


#  keyword argument,

sum(b = 3,a = 2)


#default argument,

def sum(a,b = 3):
    print(f"the sum of your number is {a + b}")

sum(2)


# Q make a function to check pallindrome

def pallindrome(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print(f"{st} is pallindrome")
    
    else:
        print(f"{st} not a pallindrome")
    


pallindrome("ashish")

pallindrome("naman")


