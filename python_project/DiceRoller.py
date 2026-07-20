import random

def rolldice():
    return random.randint(1,6)



while True:
    choice  = input("Press Enter to roll the dice  ")

    number = rolldice()
    print(f"You rolled: {number}")