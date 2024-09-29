import random, time
from colorama import Fore, Back, init, Style

fore_colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.BLACK]
back_colors = [Back.RED, Back.GREEN, Back.BLUE, Back.YELLOW, Back.MAGENTA, Back.CYAN, Back.WHITE, Back.BLACK]

print(Style.BRIGHT+"START!!!***")
while True:
    print(Style.BRIGHT + random.choice(fore_colors) +( "*" * random.randint(10,45)))
    time.sleep(random.random() * 0.13)