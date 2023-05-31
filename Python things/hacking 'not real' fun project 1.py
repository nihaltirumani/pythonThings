import time
import random

def hack(name):
    wait_time = random.random() + 0.50
    print("Hacking", name, "in progress...")
    time.sleep(wait_time)
    print("You hacked", name + "!")

name_to_hack = input("Who do you want to hack? ")
hack(name_to_hack)
#modules used: random, time