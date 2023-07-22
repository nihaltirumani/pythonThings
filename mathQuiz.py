# Importing modules.
import random
import time

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