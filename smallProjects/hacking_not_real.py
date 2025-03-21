import time
import random

def hack():
    name_to_hack = input("Who do you want to hack? ")
    wait_time = random.random() + 0.50
    print("Hacking", name_to_hack, "in progress...")
    time.sleep(wait_time)
    print("You hacked", name_to_hack + "!")

hack()
#modules used: random, time