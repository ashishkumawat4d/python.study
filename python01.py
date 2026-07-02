print("hello world ")


#                comments (we have to use '#' for writing a comment in python)


#                Variables in python
       
       
#                In python Variables are used as a storage to store things in
#                python (we will see later what we have to store)
#                You can write anything as a variable name.




Name = "ashish"
Age = 20


#                 You can not use numbers at variable start
#                 You can not use spaces in variables.
#                 You should not use special characters in variables.




#                 Data Types in python
#                 
#                 
#                 Data types are the things we store in Variables and it
#                 defines what data type variables are.
#                  Python has built-in data types for different kinds of data.
#                 
#                 1.Numbers
#                 Integer
#                 Float
#                 Complex
#                 - All the numbers excluding decimal places and fraction.
#                 - All the decimal numbers and fraction values are Float.
#                 - Numbers with real and imaginary parts are complex.
#                 
#                 
#                 2.Strings - This is used to store anything in python, literally anything
#                 that are available on your keyboard.
#                 You have to use quotes to store anything and it will be
#                 considered as string. You can use double Quotes (“”) or
#                 single quotes (‘’) to store both works same.
#                 
#                 
#                 3.Boolean
#                 Boolean - Theres nothing much to say this is the data type which
#                 will and always give the result of True and False.

#                 Strings and type conversion
#                 
#                 
#                 -> You know what strings are but you must also know string
#                 take more space than other data types like int, float etc
#                 -> This happens because String stores every character with
#                 their own Unicode
#                 -> is a universal character encoding standard that
#                 assigns a unique number (code point) to every character,
#                 regardless of language
#                 ->Like “A” unicode is 65 and “ ” this emoji unicode is 128522,
#                 you can check them by using ord() function in python and
#                 convert them back using chr() function.

#                 how to find unicode



#                 1.char to unicode(A---->65)
a = "A"
print(ord(a))

#                 2.unicode to char(65---->A)

a = 65
print(chr(a))
          
#                 You must have thought there are so many characters in a
#                 string but can you access everyone.

#                 Yes thats possible using indexing. Indexing starts from 0 and
#                 goes till the number of characters you have.


b = "xyz"

#                 index: x=0   y=1   z=3

#                 There is negative indexing as well and it starts from -1, but
#                 the starting position is from the back of the string

c = "abc"           

#                 negative index: c=-1  b=-2  a=-3

#                 We can obtain the output using the index.

d = "ashish"

print(d[0])  # a
print(d[1])  # s
print(d[2])  # h
print(d[3])  # i
print(d[4])  # s
print(d[5])  # h


