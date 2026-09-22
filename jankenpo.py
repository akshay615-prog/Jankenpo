import random
options = ["stone", "paper", "scissors"]

def game():
    while True:
        user = input("Enter stone/paper/scissors or exit: ").lower()

        if user == "exit":
            break

        if user not in options:
            print("Invalid choice")
            continue

        comp=random.choice(options)

        print("Computer:", comp)

        if user == comp:
            print("Draw")
        elif (user=="stone" and comp == "scissors") or (user == "paper" and comp == "stone") or (user == "scissors" and comp == "paper"):
            print("You Win")
        else:
            print("You Lose")

game()
