#                             LOOPS





#              Loops in python
            
#              Loops in Python allow us to execute a block of code multiple
#              times without rewriting it
              
#              Types of loops
              
#              There are 2 types of loops in python. For and While loop.
              
              
              
#              1.For loop
              
              
              
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


#              1.FOR LOOP

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
