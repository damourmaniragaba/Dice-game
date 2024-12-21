import random

while True:
    choice= input("roll a dice(y/n):").lower()
    if choice == "y":
        die1 = random.randint(1,6)
        die2= random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice == "n":
        print("thank your for your time and have a good one!")
    else:
        print("invalid choice")


