# Importing varibles.
import random
import modules.nMods as n

# Variables.
random_number = 0
user_number = 0
trys = 0

# Introduction.
n.printsec("Welcome to guess the number!.", 1)
n.printsec("A random number is chosen.", 1)
n.printsec("You have to guess the number.", 1)
n.printsec("So, get ready in...", random.random() + random.random())
print("NOW!!")

# Game loop.
def repeat():
    global trys
    user_number = int(input("Enter your number: "))

    if user_number == random_number:
        print("You won!")
        print("The correct answer is", random_number)
        print("You did", trys, "trys")
    elif user_number > random_number:
        print("Your guessed number is above.")
        trys += 1
        repeat()
    elif user_number < random_number:
        print("Your guessed number is below.")
        trys += 1
        repeat()

random_number = random.randint(1, 100)
repeat()