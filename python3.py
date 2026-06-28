#                     Conditional statements


#           Conditional statements in Python allow decision-making by
#           executing different blocks of code based on conditions




#           Types of conditional statements

  
#           Generally there are 3 types of variation in conditional
#           statements 

#           if - Executes if the condition is True*
#           if-else - Executes if True, another if False
#           if-elif-else - Checks multiple condition in sequence.

#           EXAMPLE

#           1.If statement



a = 13

if a > 12:
    print("i will do task A")



#           2.If else statement

a = 12

if a > 0:
    print("i will do task A ")

else:
    print("i will do task B")






a = -12

if a > 0:
    print("i will do task A ")

else:
    print("i will do task B")







money = int(input("provide me the money :"))

if money == 10:
    print("i will buy choco bar")

else:
    print("i will buy cup cake")





#           3.if-elif-else


money = int(input("give me money :"))

if money < 10:
    print("i will have a choco bar give me more next time :( ")

elif money == 10:
    print("i will have a :) ")

else:
    print("i will buy whole store :))) ")



#                       Some Questions on Conditional


#   Q1. Accept two numbers and print the greatest between them.


num1 = int(input("enter the value of num1 :"))
num2 = int(input("enter the value of num2 :"))
if num1 > num2:
    print("num1 is greater thenmn num2")

elif num1 < num2:
    print("num1 is less then num2")

else:
    print("both the number are same")



#  Q2. Accept the gender from the user as char and print the
#     respective greeting message

gen = input("pless tell your gender as character M or F :")

if gen == 'M':
    print("good morning SIR")

elif gen == 'F':
    print("goog morning mam")

else:
    print("why are you gay")


#  Q3. Accept an integer and check whether it is an even number
#      or odd.


num = int(input("please enter the value"))

if num %2 == 0:
    print(" even number ")

else:
    print("odd number")





 
#  Q5. Accept a year and check if it a leap year or not

     # A leap year is a calendar year containing 366 days instead of the usual 365
     # It is evenly divisible by 4.


year = int(input("tell your year"))
    
if year%4  == 0:
    print("its a leap year")

else:
    print("its not a leap year")




#                     If- elif ladder



#           You cna also create if elif ladder using multiple conditions of
#           elif

#           EXAMPLE:
#                  take the input of temperature in celsius:



#                  Below 0°C → "Freezing Cold"

#                  0°C to 10°C → "Very Cold"

#                  10°C to 20°C → "Cold"

#                  20°C to 30°C → "Pleasant"

#                  30°C to 40°C → "Hot"

#                  Above 40°C → "Very Hot"


temp = int(input("please tell the temprature"))

if temp == 0:
    print("Freezing Cold")

elif 0 < temp < 10:
    print("Very Cold")

elif 10 < temp < 20:
    print("cold")

elif 20 < temp < 30:
    print("Pleasant")

elif 30 < temp < 40:
    print("hot")

elif temp > 40:
    print("Very Hot")






