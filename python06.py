#             While loop

#      The while loop repeats a block of code as long as a condition
#      is True. It is useful when the number of iterations is unknown
#      before execution
#      
#      it also have break, continue and else.

# EXAMPLE

a = 0

while a <= 30:
    print(a)
    a = a + 1
     


#      While loop questions





#  Q1 Separate each digit of a number and print it on the new line






a = int (input("tell your number"))

while a > 0:
    print(a % 10)
    a = a//10








#  Q2 Accept a number and print its reverse






a = int(input("tell your number to reverse"))

rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a //10

print(rev)









# Q3 Accept a number and check if it is a pallindromic number (If
#    number and its reverse are equal)

a = int(input("pallindromic number check "))

copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a //10

if copy == rev:
    print("pallindromic number")

else:
    print("not a pallindromic number")




# Q4 Create a random number guessing game with python.

import random

num = random.randint(1,10)

tries = 0


while True:
  guess = int(input("please guess your number"))

  if num == guess:
      tries +=1
      print(f"you are right, you guessed the number in {tries} tries")
      break
  
  elif num < guess:
      print("go a little low ")
      tries +=1

  elif num > guess:
      print("go a little higher")
      tries +=1


  else:
     tries +=1
     print("you are wrong")
    



    

