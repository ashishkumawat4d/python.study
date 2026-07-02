#               For Loop questions

#  Q1 Accept an integer and Print hello world n times

n = int(input("enter the value of n"))

for i in range(n):
    print("hello!,world")     


#  Q2 Print natural number up to n    

n = int(input("enter your value"))

for i in range(1,n+1,1):
    print(i)

    
#  Q3 Reverse for loop. Print n to 1

n = int(input("enter your value"))

for i in range(n,0,-1):
    print(i)



#  Q4 Take a number as input and print its table

n = int(input("which table you want"))

for i in range(1,11):
    print(f"({n*i})")





# Q5 Sum up to n terms

n = int(input("(Sum up to n terms),enter your value"))

sum = 0

for i in range(1,n+1):
    sum = sum + i

print(f"your sum is {sum}")




#  Q5 - Factorial of a number








n = int(input("(Factorial of a number),enter your number"))

fact = 1

for i in range(1,n+1):
    fact = fact * i

print(f"your factorial is {fact}")









