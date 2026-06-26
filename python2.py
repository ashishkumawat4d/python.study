#                 String Slicing
#                 
#                 You know how to access characters in string. But there are
#                 slicing option as well.

#                 Slicing means cutting out a slice from string and this is also
#                 done using index values

#                 So here we have start , stop and steps position and keep a
#                 note if we use stop at 4 it will slice till 3 only.
 

#                a[start point:stop point:steps]

a = "ashish coder"

print(a[0:6:1])
#         ^--> stop index(5) se 1 extra likhna pdega 
#   it will print "ashish" only this is called string slicing

# if we want to print coder throgh slicing it will be like this

print(a[7:12:1])
#OR
print(a[7::1])

#               Type conversion
#               
#               For understanding type conversion you have to look at these
#               things
#               
#               int() float() str() bool()
#               
#               There are more functions like this but these are 4 main
#               function, looking at these functions you can guess these are
#               used to convert one data type to another


#               example 1

 
a = 12
#type of a is int

a = str(a)

print(type(a))

#              example 2

a = "12"
#type of a is string

a = int(a)

print(type(a))



#         Type conversion types
#         
#         There are 2 types of conversion Implicit and Explicit
#          
#         
#         Implicit                                      Explicit
#         
#         In this, python automatically                 In this we as a user use in build
#         converts data from one data                   type to anotherh
#         type to another                               You have seen the example at
#          You have already seen the                    previous page.
#         example before
#                                                       int()        Integer
#                                                       float()      Float
#                                                       complex()    Complex
#                                                       str()        String
#                                                       list()       List
#                                                       tuple()      Tuple
#                                                       set()        Set
#                                                       dict()       Dictionary
#                                                       bool()       Boolean


#                                Input and output

#               
#               
#           You probably know till now, how to provide the output of the
#           code you have written and that is with print() function
name = "ashish"
age = "20"

print(name,age)

#           There is no other functions to provide the result on the
#           terminal we just have to use print() function



#                         FORMATED STRING



#           Now when providing the output we can use variables in print
#           statement using a formatted string as shown in the below
#           example.

song = "star boy"
singer = "The weekend"

print(f"My favorite song is {song} by The {singer}.")
#     ^---- to use formative string we have to use f first


#           INPUT
#        
#           But the main question is how to ask user for some
#           information. 

#           For example there is a user and you want to ask the age of
#           that user, how can you do so, it’s easy using input()

#           Now the default data type of input is always string reason is
#           simple you can store anything in string.

#           You have to manually convert the data type of input
#           statements.

name = input("hello what is your name   ")
print(f"hello,{name}" )



#                            OPERATORS


#           Operators are symbols that perform operations on variables
#           and values. Python has several types of operators for
#           different tasks like arithmetic, comparison, logical operations,
#           and more

#           Lets see every operators one by one.


#              [1]  Arithmetic operators


#              Arithmetic operators perform mathematical operations like
#              addition, subtraction, multiplication, division, etc

#              There are 7 types of arithmetic operator.G
             
#              addition          -      '+'
             
#              subtraction       -      '-'  
               
#              multiplication    -      '*'   
            
#              division          -      '/' 
           
#              Floor division    -      '//'      
           
#              modulus           -      '%'       
            
#              Exponentiation    -      '**'



#              EXAMPLE

#              1.addition 
a = 50
b = 13

print(a + b)

#              2.subtraction 

print(a - b)

#              3.multiplication

print(a * b)

  
#              4.division

print(a/b)

#              5.Floor division
#                               operator that divides two numbers and rounds the result down
#                               to the nearestwhole number (towards negative infinity)    

print(a//b) 
              

#              6.modulus
#                       It returns the remainder after dividing one number by another

print(a % b)

#              7.Exponentiation
#                              It is used to raise a number to the power of another number.

print(5**2)

                          
                          
#                          Operator Precedence

#               Python Operator Precedence (Highest to Lowest)
#               
#               1. ()                       Parentheses (Brackets)
#               2. **                       Exponentiation (Power)
#               3. +x, -x, ~x               Unary Plus, Unary Minus, Bitwise NOT
#               4. *, /, //, %              Multiplication, Division, Floor Division, Modulus
#               5. +, -                     Addition, Subtraction
#               6. <<, >>                   Bitwise Left Shift, Right Shift
#               7. &                        Bitwise AND
#               8. ^                        Bitwise XOR
#               9. |                        Bitwise OR
#               10. ==, !=, >, <, >=, <=,
#                   is, is not, in, not in  Comparison, Identity, Membership
#               11. not                     Logical NOT
#               12. and                     Logical AND
#               13. or                      Logical OR
#               14. =, +=, -=, *=, /=,
#                   //=, %=, **=            Assignment Operators
#               15. lambda                  Lambda Expression (Lowest)


                

#                [2]   Assignment operator

#               Assignment operators are used to assign values to variables.
#               A basic assignment operator is simple =.

#                   compound Assignment operator


#               Compound assignment operator

#               Compound assignment operator combines arithmetic
#               operations with assignment

#               But first you have to understand how things work when we
#               reassign variables in python and also reassigning variables
#               with addition, subtraction etc

#                +=     Add and assigD
#                -=     Subtract and assigD
#                *=     Multiply and assignA
#                /=     Divide and assigD
#                //=    Floor divide and assigD
#                %=     modulus and assigD
#                **=    Exponentiation and assign
#               
#              Example

a = 20

a = a + 20

a = a + 20

print(a)

#OR

a = 20

a += 20

a += 20

print(a)





#                [3]  Comparison operator

#            Comparison operators, also called relational operators, are
#            used to compare two values

#            Comparison operators will always provide Boolean result that
#            is True and False


#            comparison operators are as follow

#              ==  Equal to
#              !=  Not Equal to
#              >   Greater than
#              <   Less than 
#              >=  Greater than or equal to
#              <=  Less than or equal to


#            Comparison operators will work with numbers but you can
#            use them with strings as well.

#            EXAMPLE
a = 12
b = 12

print(a == b)   # it will give the output in boolen (true or false)
print(a != b)



#            Strings will be comparing the Ascii values of string.


print(ord("A"))
print(ord("B"))

print("A" < "B")

#            it will compare throgh Ascii values


#            Logical operators

#           Logical operators in Python are used to combine multiple
#           conditions and return a Boolean result (True or False)

#           There are 3 types of logical operator

#           and - Return True if both condition are Tru
#           or - Return True if at least one condition is True
#           not - Reverse the boolean value

#           EXAMPLE 

#           1. AND

print(12 > 11 and 13 > 12)
#     true        true  -----> out(true)

#            (If even one condition is False, the entire expression becomes False)
           
#            print(true and true and false) ---> out(false)



#            2. OR


print(12<11 or 13<12 or 12>11)  

#           (If even one condition is False, the entire expression becomes False)


#            3. NOT

print(not 12 == 12)   # (Reverse the boolean value)----> out(false)

