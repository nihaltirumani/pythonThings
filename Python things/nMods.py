# Modules.
import random
import time

def split_words(string):
    index = 0
    while index != len(string):
        print(string[index])
        index += 1


def random_colour_teller(pr):
    if pr == "print":
        color=["red","yellow","orange","green","blue","voilet","purple","white","black","cyan","gray","pink","brown","maroon","silver","gold"]
        print(random.choice(color))
    elif pr == "return":
        color=["red","yellow","orange","green","blue","voilet","purple","white","black","cyan","gray","pink","brown","maroon","silver","gold"]
        return random.choice(color)
    else:
        print("type \"print\" to print the function or type \"return\" to return the function.")


def caluculator():
    answer=input("what caluculation want to do? ")
    if answer=="addition":
        num1=int(input("first number "))
        num2=int(input("second number "))
        print(num1+num2)
    if answer=="subtraction":
        num1=int(input("first number "))
        num2=int(input("second number "))
        print(num1-num2)
    if answer=="multiplycation":
        num1=int(input("first number "))
        num2=int(input("second number "))
        print(num1*num2)
    if answer=="division":
        num1=int(input("first number "))
        num2=int(input("second number "))
        print(num1/num2)


def table_maker():
    table_number=int(input("What table do you want to be generated? "))
    table_times=int(input("How many times? "))
    index=0

    while not index==table_times:
        print(table_number,"*",index+1,"=",table_number*(index+1))
        index+=1


def generate_password():
    # varibles of different characters
    lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_-+=\"{ }'[]:;\<>,.?/"

    # other varibles for generating password
    index = 0
    password = ""
    character_range = 0

    # Merge all the characters into one list
    all_characters = list(lowercase_alphabets + uppercase_alphabets + numbers + symbols)

    # asking the user for character limit and generating the output
    character_range = int(input("Character range for password (limitations from 30) : "))

    while index < character_range:
        try:
            password = password + all_characters[random.randint(0, len(all_characters))]
        except IndexError:
            print("Character limit is below 30.")
            exit()
        index += 1
    
    print("Your password is:", password)


def random_joke(pera):
    list_of_jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I used to be a baker, but I couldn't make enough dough.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What do you call a fish with no eyes? Fsh.",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "How do you organize a space party? You planet!",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "How does a penguin build its house? Igloos it together.",
            "Why don't eggs tell jokes? Because they might crack up!",
            "Why did the bicycle fall over? It was two-tired.",
            "What's brown and sticky? A stick!",
            "What did one wall say to the other wall? 'I'll meet you at the corner.'",
            "Why don't oysters donate to charity? Because they are shellfish.",
            "Why don't skeletons fight in wars? They don't have the guts!",
            "What do you call a snowman with a six-pack? An abdominal snowman.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "How do you organize a space party? You planet!",
            "Why don't seagulls fly over the bay? Because then they would be bagels.",
            "What's orange and sounds like a parrot? A carrot.",
            "Why did the math book look sad? Because it had too many problems.",
            "How do you make a tissue dance? You put a little boogie in it.",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "What did one wall say to the other wall? 'I'll meet you at the corner.'",
            "How do you catch a squirrel? Climb a tree and act like a nut.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "How does a penguin build its house? Igloos it together.",
            "Why don't eggs tell jokes? Because they might crack up!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the chicken go to the seance? To talk to the other side.",
            "What did the grape do when it got stepped on? It let out a little wine.",
            "Why don't scientists trust atoms? Because they make up everything!",
            "How does a train eat? It goes chew, chew!",
            "What's brown and sticky? A stick!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What do you call a fake noodle? An impasta.",
            "Why don't oysters donate to charity? Because they are shellfish.",
            "What's orange and sounds like a parrot? A carrot.",
            "Why did the bicycle fall over? It was two-tired.",
            "How do you catch a squirrel? Climb a tree and act like a nut.",
            "Why don't seagulls fly over the bay? Because then they would be bagels.",
            "What's the best time to go to the dentist? Tooth-hurty!",
            "Why don't skeletons fight in wars? They don't have the guts!",
            "What do you call a snowman with a six-pack? An abdominal snowman.",
            "Why did the math book look sad? Because it had too many problems.",
            "How do you make a tissue dance? You put a little boogie in it.",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "What did one wall say to the other wall? 'I'll meet you at the corner.'",
            "How do you catch a squirrel? Climb a tree and act like a nut."
        ]

    if pera == "print":
        print(list_of_jokes[random.randint(0, len(list_of_jokes)-1)])
    elif pera == "return":
        return list_of_jokes[random.randint(0, len(list_of_jokes)-1)]

def random_equation():
    random_number = random.randint(1, 4)
    if random_number == 1:
        operator = "+"
    elif random_number == 2:
        operator = "-"
    elif random_number == 3:
        operator = "*"
    elif random_number == 4:
        operator = "/"

    num1 = str(random.randint(1, 25))
    num2 = str(random.randint(1, 25))
    question = "Answer the equation: " + num1 + " " + operator + " " + num2 + " " + "=" + " "

    num1 = int(num1)
    num2 = int(num2)

    try:
        user_answer = int(input(question))
    except ValueError:
        print("Enter a number, not letters")
        exit()

    if operator == "+":
        answer = num1 + num2
    if operator == "-":
        answer = num1 - num2
    if operator == "*":
        answer = num1 * num2
    if operator == "/":
        answer = num1 / num2

    if operator == "/":
        user_answer = float(user_answer)

    if answer == user_answer:
        print("Correct answer!")
    else:
        print("Wrong answer. Try again.")
        print(answer,"is the correct answer.")


def math_quiz():
    # Varibles.
    index = 1
    operator = ""
    num1 = ""
    num2 = ""
    random_number = 0
    question = ""
    answer = ""
    user_answer = ""
    correct_answers = 0

    # Greeting the user and explaining about the game.
    print("Welcome to maths quiz!")
    time.sleep(1)
    print("There are ten equations.")
    time.sleep(1)
    print("You have to answer them correctly.")
    time.sleep(1)
    print("The more the correct, the more the points!")
    time.sleep(1)
    print("Get ready in...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Go!")

    # Game engine.
    while index < 11:

        # Generating a random operator.
        random_number = random.randint(1, 4)

        if random_number == 1:
            operator = "+"
        elif random_number == 2:
            operator = "-"
        elif random_number == 3:
            operator = "*"
        elif random_number == 4:
            operator = "/"
        
        # Generating the question.
        num1 = str(random.randint(1, 25))
        num2 = str(random.randint(1, 25))
        question = "Answer the equation: " + num1 + " " + operator + " " + num2 + " " + "=" + " "
        
        # Asking the user to answer.
        num1 = int(num1)
        num2 = int(num2)

        print("Q."+str(index))
        try:
            user_answer = int(input(question))
        except ValueError:
            print("Enter a number, not letters")
            quit()
        
        # Checking if the user answer is right or not.
        if operator == "+":
            answer = num1 + num2
        if operator == "-":
            answer = num1 - num2
        if operator == "*":
            answer = num1 * num2
        if operator == "/":
            answer = num1 / num2

        if operator == "/":
            user_answer = float(user_answer)

        if answer == user_answer:
            print("Correct answer!")
            correct_answers += 1
        else:
            print("Wrong answer.")
            print(answer,"is the correct answer.")
        
        index += 1

    print("You got", correct_answers, "point!")


def random_game_idea():
    list_of_types0 = ["Cool", "Boring", "Useful"]
    list_of_types1 = ["Input", "Non-input"]
    list_of_types2 = ["AI", "manual"]
    list_of_types3 = ["Fun", "Next level", "Awesome"]
    list_of_types4 = ["No modules", "Random", "Time", "Random and time"]

    print(list_of_types0[random.randint(0,2)])
    print(list_of_types1[random.randint(0,1)])
    print(list_of_types2[random.randint(0,1)])
    print(list_of_types3[random.randint(0,2)])
    print(list_of_types4[random.randint(0,3)])


def commander():
    print("Welcome to commander. Type commands to make an action. Type \'help\" for more.")

    run = True
    command_list = ["help", "end", "print"]

    while run:
        command = input("")
        if command in command_list:
            if command == command_list[0]:
                print("Here is the list of all commands", command_list)
            elif command == command_list[1]:
                run = False
            elif command == command_list[2]:
                command = input("input: ")
                print(command)
        else:
            print("Invlid command")



def practice_my_name():
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
        nonlocal points
        nonlocal nihal_time
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


def printsec(str, sec_num):
    print(str)
    time.sleep(sec_num)


def guess_the_number():
    # Variables.
    random_number = 0
    user_number = 0
    trys = 0

    # Introduction.
    printsec("Welcome to guess the number!.", 1)
    printsec("A random number is chosen.", 1)
    printsec("You have to guess the number.", 1)
    printsec("So, get ready in...", random.random() + random.random())
    print("NOW!!")

    # Game loop.
    def repeat():
        nonlocal trys
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