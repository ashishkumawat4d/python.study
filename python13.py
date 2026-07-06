# ----------------------- ADVANCE STUFF --------------------------------------------


#         1.Decorator
        
#         A decorator is just a function that modifies another function
#         without changing its actual code.
        
        
        
        
#         For creating a decorator you first have to create a decorator
#         functions and then inside that we will create a wrapper.


#         Example:

def decorate(func):
    def wrapper():
        print("i will print before function")
        func()
        print("i will print after the function")

    return wrapper


@decorate
def function():
    print("hello , i am the function")

function()
   







def decorate(func):
    def wrapper(a,b):
        print("the addition to your numbers are")
        func(a,b)
        print("thank you i hope you liked it")

    return wrapper


@decorate
def addition(a,b):
    print(f"{a+b}")

addition(12,11)
   








#          2.Args and Kwargs


#     *args and **kwargs are special parameters in Python that 
#     allow a function to accept a variable number of arguments.


#     A. *args (Variable Positional Arguments)

#    *args allows a function to accept any number of positional arguments.

#     args is a tuple.
#     You can pass 0, 1, or many positional arguments
#     The name args is just a convention. You can write *numbers, *values, etc


def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(f"your sum is {sum}")

addition(12,32,34,23,23)

addition(1,2,3,4,5,5,7,8,8,6,7865,7574,5,435,4,43,5,)




#      B. **kwargs (Variable Keyword Arguments)

#     **kwargs allows a function to accept any number of keyword arguments.



#       kwargs is a dictionary.
#       Arguments are passed using key = value.
#       The name kwargs is also just a convention.



def info(**kwargs):
    print("your information is :\n\n")
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")


info(Name = "Ashish",age = "20",height = "184 cm")






# Example of decorator +  Args and Kwargs




def decorate(func):
    def wraper(*args,**kwargs):
        print("your total is ")
        func(*args,**kwargs)
        print("thanks")

    return wraper

    



@decorate
def addition(a,b):
    print(f"your sum is :{a + b}" )



addition(12,12)






#      3.List, Dictionary and set comphrehension



#      All of these Comprehensions are used to create List, Dictionary
#      and set. But you don’t have to use multiple lines of code for loops
#      and If-Else statements.

#      list -

l = [ i for i in range(1,21) if i % 2==0]

print(l)



#      Dictionary -


l = {i : i**2 for i in range(1,10)}

print(l)







#       4.Lambda functions



# A lambda function is an anonymous, inline function defined using
# the lambda keyword.

# It's often used for short, simple functions that are used only once
# or temporarily.

# You can have multiple arguments but there will be only one
# expression.



# example:

# normal method

def addition  (a,b):
    print(a + b)


addition(12,13)





#       using lambda function





addition = lambda a,b : a + b

print(addition(12,13))







#       using if else in lambda function


check = lambda a : "even" if a % 2 == 0 else "odd"

print(check(12))







#             5.Map filter and zip






#      Map is used for applying a function to multiple items.

#      Takes a list (or any sequence)

#      Applies the same function to every item in that list.









#        A. map



a = [1,2,3,4,5,6]

result = map(lambda x : x*2,a )

print(list(result))


#         You can use it with lambda or normal functions.


a = [1,2,3,4,5]

def double(x):
    return x*2

result = map(double,a)

print(list(result))

#        Use map() when you want to transform every item in a list.
       
#        It doesn’t remove or skip items (that’s what filter() does).




#           B. Filter



#        Filter as the name suggest is used to filter out the stuff.

#        2 Takes a list (or other sequence)

#        Checks each item using a function (a test)

#        Keeps only the items that pass the test (i.e., return True)


#        Example:


def even(x):
    if x % 2 ==0:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]

result = filter(even,a)

print(list(result))


#      OR


a = [1,2,3,4,5,6,7,8,9]

result = filter(lambda x : True if  x%2 == 0 else False , a)


print(list(result))




#                 Modules and packages




#        Module is just a single file containing code and we can use this
#        file code in other file.

#        A single Python file (.py)

#        2 Contains functions, variables, or classe.

#        Used to organize and reuse code.




#        Example:
#        (i have created a file Modules.py )

import Modules

print(Modules.total(12,13))




#        Python comes with lots of ready-to-use modules like -

#        2 math (for math operations)
#        2 random (for generating random numbers)
#        2 datetime (for date and time)

#        Example:


import math

print(math.sqrt(4))





#        package




#        A package is a folder that contains one or more modules (Python
#        files). It may also contain sub-packages.
       
       
#        There are third party packages as well like numpy, pandas,
#        matplotlib etc. and we have to install all of these.


#        
