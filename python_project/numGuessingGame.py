import random

num = random.randint(1,10)

tries = 0

while True:
     
     guess = int(input('please guess a number'))
     
     if guess == num:
         tries = tries + 1
         print(f"you are right, you guessed the number in {tries} tries")
         break
     
     elif guess > num:
         tries = tries + 1
         print("you are wrong, go a little low")
     
     elif guess < num:
         tries = tries + 1
         print("you are wrong, go a little higher")
     


