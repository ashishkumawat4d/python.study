#                             LOOPS





#              Loops in python
            
#              Loops in Python allow us to execute a block of code multiple
#              times without rewriting it
              
#              Types of loops
              
#              There are 2 types of loops in python. For and While loop.
        


#              1.For loop
              
              
#              A.FOR LOOPS FOR NUMBERS
              
#              Range function
              
              
#              Before understanding for loops you should know how range
#              function works
              
#              The range() function is used to generate a sequence of
#              numbers, which is commonly used in loops
              
#              Syntax of range function is simple range(start, stop, steps)
              
#              you have 3 points from where you want to start, till where
#              you want to stop and how many steps you want
              
#              If you don’t mention start point the default value will be 0
              
#              if you don’t mention the steps the default steps will be 1.
              
#              you have to mention the stop point otherwise the range
#              function will not work.




# range(start, stop, steps)

a = range(1, 20, 1)


for i in a:
    print(i)



# OR




for i in range(1, 20, 1):
    print(i)



# lets print a table of five



for i in range(5, 51, 5):
    print(i)



# lets print a table of nth number




n = int(input("which table you want"))

for i in range(n,(n*10)+1,n):
    print(i)






#           B.FOR Loops for strings




#            Loops for strings work slightly differently. You can iterate
#            through a string in two ways
#            
#            > Using index values
#            > Iterating directly over the string
#            
#            Iterating using the index values, Now we know that index
#            values are numbers and for numbers we again have to use
#            range function.









a = "ashish"

for i in range(6):
    print(a[i])




a = "Ashish is cool!!"

for i in range(len(a)):
    print(a[i])





#                 Break continue else

#         1.BREAK


#         A The break statement in Python is used to exit a loop
#         prematurely when a certain condition is met. Once break is
#         encountered, the loop stops immediately, and control moves
#         to the next statement after the loop






for i in range(1,21,1):
    if i == 12:
        break
    else:
        print(i)
        






        
#         2.CONTINUE        
        
#         A The Continue statement skips one of the iteration and rest of
#         the iterations will run








for i in range(1,21,1):
    if i == 12:
        continue  #(now it will skip 12)
    else:
        print(i)









#         3.ELSE


#         A You have seen the else statement used with if, but it can also
#         be used with loops. When else is used with a loop, it only
#         executes if the loop completes without encountering a break
#         statement. If break is executed, the else block will not run.


for i in range(1,21,1):
    if i == 12:
        print("break statement is executed")
        break
    print(i)

else:
    print(i and ("break statement is not executed"))





#               For Loop questions

#  Q1 Accept an integer and Print hello world n times

n = int(input("enter the value of n"))

for i in n == range(n+1):
    print("hello!,world")         

    