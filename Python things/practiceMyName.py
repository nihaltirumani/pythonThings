# Importing modules.
import time

# Varibles.
difficulty = None
nihal_time = 0
nihal = None
points = 0

# Functions.
def printsec(str, sec_num):
    print(str)
    time.sleep(sec_num)

def times(times):
    global points
    global nihal_time
    while nihal_time < times:
        nihal = input("")
        if nihal == "nihal":
            points += 1
        elif nihal == "end":
            quit()
        else:
            print("You wrote wrong.")
        nihal_time += 1
    print("You got", points, "points.")

# Introduction.
printsec("Welcome to practice my name!", 1)
printsec("My name is nihal.", 1)
printsec("In this game, you have to write my name.", 1)
printsec("With no mistakes.", 1)
printsec("If you want end in the middle of the game, just write \"end\"", 1)
printsec("There are three types of difficulties:", 1)
printsec("1.Easy = 25 times.", 1)
printsec("2.Medium = 50 times.", 1)
printsec("1.Hard = 100 times.", 1)
printsec("So, good luck.", 1)

# Selecting difficulties.
print("Choose your difficulty:\n1.Easy\n2.Medium\n3.Hard")

difficulty = input("")

if difficulty.lower() == "easy":
    times(25)
if difficulty.lower() == "medium":
    times(50)
if difficulty.lower() == "hard":
    times(100)
