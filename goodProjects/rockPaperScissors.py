import random

def check(move1, move2):
    if user == state[move1] and ai == state[move2]: return True

def win():
    if check(2, 1) or check(0, 2) or check(1, 0):
        print("You won!")
    elif user == ai:print("Draw!")
    else:print("You lost!")

state = ["rock", "paper", "scissors"]
ai = None
user = None

ai = state[random.randint(0, 2)]
user = int(input("What do you want to choose:\nRock     (1)\nPaper    (2)\nScissors (3)\n"))
if user > 3:
    print("Only numbers from 1-3.")
    exit()

user =  state[user - 1]

print(f"You choose: {user}")
print(f"AI choose: {ai}")

win()