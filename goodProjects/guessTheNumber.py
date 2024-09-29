# Importing varibles.
import random
import time

# Variables.
random_number = 0
user_number = 0
trys = 0

# definitions
def printsec(str, sec):
    print(str)
    time.sleep(sec)
    
# Introduction
printsec("Welcome to guess the number!.", 1)
printsec("A random number is chose", 1)
printsec("You have to guess the number.", 1)
printsec("So, get ready i..", random.random() + random.random())
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