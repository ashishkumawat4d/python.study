import random

choices = ["rock", "paper", "scissors"]

def winner(user,computer):
    if user == computer:
        return "it's a Tie"
    elif(
        (user == "rock" and computer == "scissors") or 
        (user == "paper" and computer == "rock")  or
        (user == "scissors" and computer == "paper")

    ):
        return "you win!"
    
    else:
        return "computer win!"


while True:

    user = input("Enter Rock, Paper or Scissors ")

    if user not in choices:
        print("Invalid Choice!")
        continue

    computer = random.choice(choices)

    print(f"You chose      : {user}")
    print(f"Computer chose : {computer}")

    result = winner(user,computer)

    print("result:",result)

    
